from fastapi import APIRouter
from pydantic import NegativeInt, PositiveInt

from microwave.application.schemas import Microwave
from microwave.application.service import ApplicationService

# from auth_bearer import JWTBearer

router = APIRouter()


@router.get("/state", response_model=Microwave)
async def read_state():  # token: str = Depends(JWTBearer())):
    service = ApplicationService()
    return service.get_state()


@router.post("/power", response_model=Microwave)
async def update_power(power: NegativeInt | PositiveInt):
    service = ApplicationService()
    return service.update_power(power)


@router.post("/time", response_model=Microwave)
async def update_counter(time: NegativeInt | PositiveInt):
    service = ApplicationService()
    return service.update_counter(time)


@router.post("/cancel", response_model=Microwave)
async def cancel():
    service = ApplicationService()
    return service.cancel()
