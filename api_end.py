from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import uvicorn
app= FastAPI()


items =["first","second","third"]

@app.post("/item")
def add(itm:str):
    items.append(itm)
    return items 

class pr(BaseModel):
    title: str
    body:str
    answer: Optional[int]=None

@app.post("/")
def f(req:pr):
    if(req.answer==0):
        print("hello")
    return f"hello this is the title {req.title} and this is the body {req.body} and this is the optional feild"


@app.get("/")
def root():
    return {"hello":"world"}


@app.get("/i/{id}")
def s(id:int) -> str:
    return items[id]

if __name__ =="__main__":
    uvicorn.run(app,host="127.0.0.1",host=8000)
