from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time

app = FastAPI()

SUPPORTED_VERSION = "1.0.0"

class RequestData(BaseModel):
    x: int
    version: str

def F(x: int) -> int:
    return x * x

@app.post("/run-godot")
async def calculate(data: RequestData):

    # Version validation
    if data.version != SUPPORTED_VERSION:
        raise HTTPException(
            status_code=426,
            detail={
                "status": "error",
                "message": "Unsupported API version",
                "received": data.version,
                "supported": SUPPORTED_VERSION
            }
        )

    time.sleep(1)

    result = F(data.x)

    return {
        "result": result,
        "status": "success",
        "version": SUPPORTED_VERSION
    }