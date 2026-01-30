from pydantic import BaseModel

class GetPredictionOfHousePrice(BaseModel):
    crim:float
    zn:float
    indus:float
    chas:int
    nox:float
    rm:float
    age:float
    dis:float
    rad:int
    tax:float
    ptratio:float
    b:float
    lstat:float