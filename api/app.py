from starlette.middleware.cors import CORSMiddleware

from auth.router import router as auth_router
from fastapi import FastAPI
from microwave.application.rest import router as rest_router
from microwave.domain.exceptions import BusinessRuleValidationException
from starlette.requests import Request
from starlette.responses import JSONResponse

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

origins = [
    "http://localhost:3000",
    "http://localhost:8001",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(BusinessRuleValidationException)
async def unicorn_exception_handler(
    request: Request, exc: BusinessRuleValidationException
):
    return JSONResponse(
        status_code=422,
        content={"error": f"{exc}"},
    )
