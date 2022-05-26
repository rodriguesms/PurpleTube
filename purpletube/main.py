import uvicorn
from fastapi import FastAPI
from .routers import movie

app = FastAPI()
app.include_router(movie.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
# fun
def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("purpletube.main:app", host="0.0.0.0", port=8000, reload=True)