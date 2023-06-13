from fastapi import Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from typing import Any, Field
from ..service import Service, get_service
from . import router


class CreateShanyrakRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str

class CreateShanyrakResponse(AppModel):
    id: Any = Field(alias="_id")

@router.post("/", response_model=CreateShanyrakResponse)
def create_shanyrak(
    input: CreateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
)-> CreateShanyrakResponse:
    shanyrak_id=svc.repository.create_shanyrak(jwt_data.user_id, input.dict())

    return CreateShanyrakResponse(id=shanyrak_id)

