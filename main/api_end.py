from fastapi import FastAPI, HTTPException, Request
from typing import Optional
from pydantic import BaseModel
import uvicorn
from pydanticModels import blog
import json
from fastapi.responses import JSONResponse
app= FastAPI()


@app.post("/")
async def func(request:Request):
    data = await request.json()  


    output_file = "saved_data.json"

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    try:
        

        for i in data:
            print(type(i["content"]))
            if(type(i["content"])==list):
                print(1)
                if(i["content"][0]["type"] !="Microsoft.SecurityInsights/dataConnectors"):
                    return JSONResponse(status_code=200, content={
                            "status": "failed",
                            "mssg": f"the type of polling file is wrong the type in file is {i["content"][0]["type"]}"
                        })
            else:
                print(2)
                if(i["content"]["type"] !="Microsoft.SecurityInsights/dataConnectors"):
                    return JSONResponse(status_code=200, content={
                        "status": "failed",
                        "mssg": f"the type of polling file is wrong the type in file is {i["content"]["type"]}"
                    })
            
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
