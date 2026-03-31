from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from app.utils.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True)
    name = Column (String)
    username = Column(String,nullable=False)
    hash_password = Column(String,nullable=False)
    email = Column(String)

    