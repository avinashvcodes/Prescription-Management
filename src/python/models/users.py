from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, BOOLEAN
from .base import BaseModel

class Users(BaseModel):

    """
    Class for mapping of users table in database
    """

    __tablename__ = "users"

    email = Column(String(100),primary_key = True,nullable = False)
    password = Column(String(60),nullable = False)
    is_admin = Column(BOOLEAN,nullable = False)

