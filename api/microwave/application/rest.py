from auth.jwt_bearer import JWTBearer
from dependencies import get_redis
from fastapi import APIRouter, Depends
from microwave.application.schemas import Microwave
from microwave.application.service import ApplicationService
from microwave.infrastructure.repositories.in_redis import RedisRepository
from pydantic import NegativeInt, PositiveInt

router = APIRouter()


@router.get("/state", response_model=Microwave)
async def read_state(redis=Depends(get_redis)):
    service = ApplicationService(RedisRepository(redis))
    return service.get_state()


@router.post("/power", response_model=Microwave)
async def update_power(power: NegativeInt | PositiveInt, redis=Depends(get_redis)):
    service = ApplicationService(RedisRepository(redis))
    return service.update_power(power)


@router.post("/time", response_model=Microwave)
async def update_counter(time: NegativeInt | PositiveInt, redis=Depends(get_redis)):
    service = ApplicationService(RedisRepository(redis))
    return service.update_counter(time)


@router.post("/cancel", response_model=Microwave)
async def cancel(token: str = Depends(JWTBearer()), redis=Depends(get_redis)):
    service = ApplicationService(RedisRepository(redis))
    return service.cancel()
