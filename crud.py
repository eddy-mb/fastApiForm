from sqlalchemy.orm import Session
import models, schemas

def create_user(db:Session, user:schemas.UserBase):
    new_user = models.User(**user.model_dump()) #pasamos el modelo pydantic como model_dump diccionario
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_email(db:Session, email:str):
    return db.query(models.User).filter(models.User.user_email==email).first()