from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())


class Subject(Base):
    __tablename__ = "subjects"

    subject_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    subject_name = Column(String, nullable=False)