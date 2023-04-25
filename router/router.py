from fastapi import APIRouter

user = APIRouter()

@user.get("/")
def root():
    return {"message": "hi, I am FastAPI with a Router"}