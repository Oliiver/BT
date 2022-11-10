from fastapi import FastAPI, status

from app.routers import v1

app = FastAPI()

app.include_router(v1.v1)
