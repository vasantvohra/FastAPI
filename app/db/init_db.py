from sqlalchemy import create_engine

from app.core.config import SQLALCHEMY_DATABASE_URI
from app.db.base_class import Base
from app.statistics import schemas, models
from app.statistics.routers.users import create_user_account

engine = create_engine(SQLALCHEMY_DATABASE_URI)  # connect_args={"check_same_thread": False} Only works with SQLITE


def init_db(db, email:str, password: str) -> None:
    # Automatically create the tables
    Base.metadata.create_all(bind=engine)

    user = db.query(models.User).first()
    if not user:
        admin_user = schemas.User(email=email, password=password, is_admin=True)
        create_user_account(admin_user, db)
