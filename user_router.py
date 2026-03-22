from fastapi import APIRouter
from starlette.exceptions import HTTPException

from models import UserCreate
import user_repository as repo

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(user:UserCreate):
    result = repo.create_user(user.name,user.email)
    return {
        "id" : result[0],
        "name": result[1],
        "email": result[2]
    }


@router.get("/{user_id}")
def get_user(user_id:int):
    user = repo.get_user(user_id)
    if not  user:
        raise HTTPException(status_code=404, detail="user not found")

    return {
            "id" : user[0],
            "name": user[1],
            "email": user[2]
            }

@router.get("")
def get_users():
    users =repo.get_users()
    user_list = []

    for user in users:
        user_list.append(
            {"id": user[0],
             "name": [1],
             "email": user[2]
             }
        )
    return user_list

@router.delete("/user_id")
def delete_user(user_id:int):
    repo.delete_user(user_id)
    return {"response" :"User Deleted Successfully"}