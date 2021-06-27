import logging
from fastapi import FastAPI

from user import models, schemas
from user.database import engine, SessionLocal
import uvicorn

from user.routers.api import api_router
from user.routers.user import create_user_account

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="RESt APIs")
logger.info("Creating initial data")
# Automatically creates Tables
models.Base.metadata.create_all(engine)
db = SessionLocal()
user = db.query(models.User).first()
if not user:
    email = 'admin'
    password = 'password'
    logger.info(f"Creating Admin account with email '{email}' and password '{password}'")
    admin_user = schemas.User(email=email, password=password, is_admin=True)
    create_user_account(admin_user, db)
logger.info("Creating endpoints")
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000, debug=True)