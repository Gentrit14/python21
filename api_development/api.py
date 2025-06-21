from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

class PersonResponse(BaseModel):
    message: str

@app.post("/users/")
async def create_user(user: User):
    return user

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int

@app.post("/create_person")
async def create_person(person: Person):
    return{"message:" f"Person {person.name} create wth age {person.age}"}

@app.post("/create_person/", response_model=PersonResponse)
async def create_person(person: Person):
    return {"message": f"Person {person.name} create with age {person.age}"}
