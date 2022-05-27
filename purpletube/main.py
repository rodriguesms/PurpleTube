import uvicorn
from fastapi import FastAPI
from .routes import movie
from .routes import user

app = FastAPI(title="PupleTube Api")

#Routes
app.include_router(movie.router)
app.include_router(user.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
# fun
def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("purpletube.main:app", host="0.0.0.0", port=8000, reload=True)