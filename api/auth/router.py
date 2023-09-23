from fastapi import APIRouter, Body

from auth.jwt_decoder import JWTDecoder
from auth.schema import UserSchema

router = APIRouter()


@router.post("/signup")
async def create_user(user: UserSchema = Body(...)):
    return JWTDecoder.encode(user.email)
