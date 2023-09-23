from fastapi import FastAPI

from application import rest

app = FastAPI()

app.include_router(rest.router, tags=["microwave"])
