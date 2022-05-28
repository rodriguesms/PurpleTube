import uvicorn
from fastapi import FastAPI

from .routes import movie
from .routes import user
from .routes import comment
from .routes import director
from .routes import actor

app = FastAPI(title="PupleTube Api")

#Routes
app.include_router(movie.router)
app.include_router(user.router)
app.include_router(comment.router)
app.include_router(director.router)
app.include_router(actor.router)

@app.get("/")
async def root():
    return {"message": "PurpleTube Api"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)