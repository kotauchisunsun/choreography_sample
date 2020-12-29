from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
import dataclasses
import uuid

class UserInput(BaseModel):
    name: str
    email: EmailStr

@dataclasses.dataclass
class User:
    id: str
    name: str
    email: EmailStr

data = dict()

app = FastAPI()

@app.post("/users/")
async def create_user(user_input: UserInput) -> User:
    user_id = str(uuid.uuid4())
    user = User(user_id,user_input.name,user_input.email)
    global data
    data[user_id] = user
    print(user_id)
    return user

@app.get("/users/{user_id}")
async def read_user(user_id: str) -> User:
    return data[user_id]

@app.delete("/users/{user_id}")
async def delete_user(user_id: str) -> None:
    del data[user_id]