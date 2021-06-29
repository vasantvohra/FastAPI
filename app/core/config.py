import secrets
SQLALCHEMY_DATABASE_URI = 'postgresql:///fast_api'  # 'sqlite:///./fast_api.db'  # 'postgresql:///fast_api'  # analytics
API_V1_STR: str = "/api/v1"
SECRET_KEY: str = secrets.token_urlsafe(32)
# 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
EMAIL = 'admin'
PASSWORD = 'password'
