import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

def start():
    print("Hello World")
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True, workers=2)
