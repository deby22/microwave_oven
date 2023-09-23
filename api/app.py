from fastapi import FastAPI

from microwave.application import rest

app = FastAPI()

app.include_router(rest.router, tags=["microwave"])
