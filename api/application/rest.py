import time

from fastapi import APIRouter

from application.service import ApplicationService

# from auth_bearer import JWTBearer

router = APIRouter()


@router.get("/state/")
async def read_state():  # token: str = Depends(JWTBearer())):
    service = ApplicationService()
    return service.get_state()
