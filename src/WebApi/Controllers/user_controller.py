from fastapi import APIRouter, FastAPI, HTTPException, Path, Body, JSONResponse
from pydantic import BaseModel
from bson import ObjectId
from Application.Contracts.iuser_service import UserServiceInterface 
from Application.UseCases.Services.user_service import UserService

from Application.UseCases.DTOs.User.create_user_dto import CreateUserDto
from Application.UseCases.DTOs.User.user_dto import UserDto

router = APIRouter()

# Initialize the user service using the interface
user_service: UserServiceInterface = UserService()  # Replace with your actual implementation

class UserCreate(BaseModel):
    telegramId: str
    telegramUsername: str
    phoneNumber: int

@router.get('/users', response_model=list[UserDto])
def list_users():
    users = user_service.list()
    return users

@router.post('/users', response_model=str)
def create_user(user_data: UserCreate):
    user = CreateUserDto(**user_data.dict())
    user_id = user_service.add(user)
    return JSONResponse(content={'message': 'User created', 'user_id': str(user_id)})

@router.get('/users/{user_id}', response_model=UserDto)
def get_user(user_id: ObjectId = Path(..., title="The user ID")):
    user = user_service.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put('/users/{user_id}', response_model=str)
def update_user(user_id: ObjectId = Path(..., title="The user ID"), user_data: UserCreate = Body(..., title="Updated user data")):
    user = CreateUserDto(**user_data.dict())
    user_service.update(user_id, user)
    return JSONResponse(content={'message': 'User updated successfully'})

@router.delete('/users/{user_id}', response_model=str)
def delete_user(user_id: ObjectId = Path(..., title="The user ID")):
    user_service.delete(user_id)
    return JSONResponse(content={'message': 'User deleted successfully'})
