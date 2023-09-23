import time

from fastapi import APIRouter


# from auth_bearer import JWTBearer

router = APIRouter()


@router.get("/state/")
async def read_state():  # token: str = Depends(JWTBearer())):
    return {"state": "state"}
