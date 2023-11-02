from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins=[
"*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/user/", response_model=schemas.UserBase)
def user_message(data: schemas.UserCreate, db: Session=Depends((get_db))):
    # user_exist = crud.get_user_email(db, email=data.user_email)
        crud.create_user(db=db, user=data)
        raise HTTPException(status_code=200, detail="Envio exitoso")

@app.get("/")
async def root():
    return {"message": "Hello World"}


