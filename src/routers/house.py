from fastapi import APIRouter
from pydantic import BaseModel
from src.services.house import runModel, runModel2
from src.dtos.house import GetPredictionOfHousePrice

house_router = router = APIRouter()

# @router.post("/price/predict")
# async def getPredictionOfHousePrice():
#     price = await runModel()

#     return price

# @router.get("/price/predict")
# async def getPredictionOfHousePriceByCrimAndRoom(crim: float, room:float):
#     price = await runModel(crim, room)

#     return price

@router.post("/price/predict")
async def getPredictionOfHousePrice2(body: GetPredictionOfHousePrice):
    price = await runModel2(body)

    return price