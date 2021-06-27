from typing import Optional

from sqlalchemy.orm import Session
from fastapi import HTTPException, APIRouter, Depends, status
from user import database, schemas, models
from user.security import get_password_hash, verify_user

router = APIRouter(prefix="/user", tags=['Users'])

get_db = database.get_db


def create_user_account(request, db):
    new_user = models.User(email=request.email, is_admin=request.is_admin)
    new_user.password = get_password_hash(request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post('/create/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(verify_user)):
    """Creates a new user account."""
    if current_user.is_admin:
        return create_user_account(request, db)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Only admins can create user accounts")


@router.put('/update/{email}', response_model=schemas.ShowUser)
def update_user(email: str, request: schemas.Login, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(verify_user)):
    """Updates the email or password of the given user email."""
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the email {email} is not available")
    if current_user.is_admin or current_user == user:
        user.email = request.email
        if request.password:
            user.password = get_password_hash(request.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Only admins can get user details")


@router.delete('/delete/')
def delete_user(email: Optional[str] = None, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(verify_user)):
    """
    Deletes a user account.
    :param email:  Query parameter only admin users can delete a user with given email
    :param db: Db in session
    :param current_user: The user requesting this operation
    :return:
    """
    user = current_user
    if current_user.is_admin and email:
        user = db.query(models.User).filter(models.User.email == email).first()
    if not user and email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Only admins can delete other users")
    db.delete(user)
    db.commit()
    return {'detail': f'User with ID: {user.id}, {user.email} deleted'}


@router.get('/{email}/', response_model=schemas.ShowUser)
def get_user(email: str, db: Session = Depends(get_db),
             current_user: schemas.User = Depends(verify_user)):
    """Fetch the user with given email."""
    if current_user.is_admin:
        user = db.query(models.User).filter(models.User.email == email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with the id {email} is not available")
        return user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Only admins can get user details")
