from fastapi import FastAPI

from api import users, filme, comentario

app = FastAPI(title="PupleTube Api")

app.include_router(users.router)
app.include_router(filme.router)
app.include_router(comentario.router)