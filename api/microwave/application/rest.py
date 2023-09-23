from auth.jwt_bearer import JWTBearer
from dependencies import get_redis
from fastapi import APIRouter, Depends
from microwave.application.schemas import Microwave
from microwave.application.service import ApplicationService
from microwave.infrastructure.repositories.in_redis import RedisRepository
from pydantic import NegativeInt, PositiveInt, BaseModel, Field

router = APIRouter()


class PowerRequest(BaseModel):
    power: NegativeInt | PositiveInt = Field(
        description="Field to update power of microwave. Positive value increase power. Negative value decrease power."
    )


class TimeRequest(BaseModel):
    time: NegativeInt | PositiveInt = Field(
        description="Field to update counter of microwave. Positive value increase counter. Negative value decrease counter."
    )


@router.get("/state", response_model=Microwave)
async def read_state(redis=Depends(get_redis)):
    service = ApplicationService(RedisRepository(redis))
    return service.get_state()


@router.post("/power", response_model=Microwave)
async def update_power(payload: PowerRequest, redis=Depends(get_redis)):
    service = ApplicationService(RedisRepository(redis))
    return service.update_power(payload.power)


@router.post("/time", response_model=Microwave)
async def update_counter(payload: TimeRequest, redis=Depends(get_redis)):
    service = ApplicationService(RedisRepository(redis))
    return service.update_counter(payload.time)


@router.post("/cancel", response_model=Microwave)
async def cancel(token: str = Depends(JWTBearer()), redis=Depends(get_redis)):
    service = ApplicationService(RedisRepository(redis))
    return service.cancel()
