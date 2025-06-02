from pydantic import BaseModel

class intial(BaseModel):
    title:str
    body:str
    i_d:int


class ready(BaseModel):
    title:str


