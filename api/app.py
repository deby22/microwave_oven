from fastapi import Depends, FastAPI

from auth.router import router as auth_router
from dependencies import get_redis
from microwave.application.rest import router as rest_router

tags_metadata = [
    {
        "name": "Microwave",
        "description": "Simple app that simulates the operation of a microwave in an office kitchen",
    },
    {
        "name": "Auth",
        "description": "Only fer testing. This is not production ready code. Use it only for generate simple JWT token",
    },
]


app = FastAPI(openapi_tags=tags_metadata)

app.include_router(rest_router, tags=["Microwave"])
app.include_router(auth_router, tags=["Auth"])
