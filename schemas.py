from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str
    user_message: str
    user_email: str

class UserCreate(UserBase):
    pass
