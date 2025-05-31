from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

user1 = User(id=1, name= 'John', age=2 , email= '123456@mail.com')
user2 = User(id=1, name= 'John', age=2)

user3 = User(id=1, name= 'John', email= '123456@mail.com')

print(user3)

class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=50)

valid_user = another_user(id=1, name= 'John')
print(valid_user)