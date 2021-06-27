from fastapi import APIRouter

from user.routers import authentication, index, user

api_router = APIRouter()
api_router.include_router(index.router)
api_router.include_router(authentication.router)
api_router.include_router(user.router)
