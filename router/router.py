from fastapi import APIRouter
from schema.user_schema import UserSchema
from config.db import conn
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash

user = APIRouter()

@user.get("/")
def root():
    return {"message": "hi, I am FastAPI with a Router"}

@user.post("/api/user")
def create_user(data_user: UserSchema):
    new_user = data_user.dict()
    new_user["user_password"] = generate_password_hash(data_user.user_password, "pbkdf2:sha256:30", 30)
    

    conn.execute(users.insert().values(new_user))

    return "Success"

@user.put("/api/user")
def update_user():
    pass