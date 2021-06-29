from fastapi import FastAPI
import uvicorn
from app.core.config import EMAIL, PASSWORD
from app.db.session import SessionLocal
from app.statistics.routers.api import api_router
from app.db.init_db import init_db

app = FastAPI(title="RESt APIs", openapi_url="/openapi.json")
init_db(SessionLocal(), EMAIL, PASSWORD)
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000, debug=True)
