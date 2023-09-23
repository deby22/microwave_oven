from fastapi import APIRouter, Depends
from pydantic import NegativeInt, PositiveInt

from auth.jwt_bearer import JWTBearer
from microwave.application.schemas import Microwave
from microwave.application.service import ApplicationService

router = APIRouter()


@router.get("/state", response_model=Microwave)
async def read_state():
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
async def cancel(token: str = Depends(JWTBearer())):
    service = ApplicationService()
    return service.cancel()
