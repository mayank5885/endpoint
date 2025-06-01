from fastapi import FastAPI, HTTPException

app= FastAPI()


items =["first","second","third"]

@app.post("/item")
def add(itm:str):
    items.append(itm)
    return items 


@app.get("/")
def root():
    return {"hello":"world"}


@app.get("/i/{id}")
def s(id:int) -> str:
    return items[id]