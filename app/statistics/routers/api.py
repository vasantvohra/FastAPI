from fastapi import APIRouter

from app.statistics.routers import login, index, users

api_router = APIRouter()
api_router.include_router(index.router)
api_router.include_router(login.router)
api_router.include_router(users.router)
