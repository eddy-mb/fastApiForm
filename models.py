
from database import Base
from sqlalchemy import  Column, Integer, String
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_email = Column(String, index=True)
    user_message = Column(String)
