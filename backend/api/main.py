import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import movie
from .routes import user
from .routes import comment
from .routes import director
from .routes import actor
from .routes import category
from .routes import avaliation
from .routes import like

app = FastAPI(title="PupleTube Api")
origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers=['*']
)
#Routes
app.include_router(movie.router)
app.include_router(user.router)
app.include_router(comment.router)
app.include_router(director.router)
app.include_router(actor.router)
app.include_router(category.router)
app.include_router(avaliation.router)
app.include_router(like.router)

@app.get("/")
async def root():
    return {"message": "PurpleTube Api"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)