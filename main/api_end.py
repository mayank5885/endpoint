from fastapi import FastAPI, HTTPException, Request
from typing import Optional
from pydantic import BaseModel
import uvicorn
from pydanticModels import blog
import json
from fastapi.responses import JSONResponse
app= FastAPI()


@app.get("/",response_model=blog.ready)
def func():
    obj = blog.intial(title="My Title", body="This is the body", i_d=101)
    return obj



@app.post("/item")
async def func(request:Request):
    data = await request.json()  # Parse JSON body to dict (no schema needed)


    output_file = "saved_data.json"

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    try:
        
        for i in data:
            if(i["content"]["type"] !="Microsoft.SecurityInsights/dataConnectors"):
                return JSONResponse(status_code=200, content={
                        "status": "failed",
                        "mssg": f"File '{f.filename}' is missing required field 'name'"
                    })
                break
        return JSONResponse(status_code=200, content={
                "status": "passed",
                "mssg": "All files passed validation ✅"
            })   

    except Exception as e:
        return JSONResponse(status_code=500, content={
            "status": "failed",
            "mssg": f"Internal server error: {str(e)}"
        })




if __name__ =="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
