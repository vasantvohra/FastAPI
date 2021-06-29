from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint
from app.db.base_class import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint('email', name='unique_email'),)

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    def __str__(self):
        return self.email, self.is_admin

    def __repr__(self):
        return f'<{self.email}: Admin({self.is_admin})>'
