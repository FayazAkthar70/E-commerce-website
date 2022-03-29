from typing import Optional
from pydantic import BaseModel

class Create_User(BaseModel):
    username :  str
    email_address : str
    password : str
    budget : Optional[int] = 1000 
    