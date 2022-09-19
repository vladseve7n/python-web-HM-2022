from pydantic import BaseModel
from typing import List, Union


class RandInt(BaseModel):
    value: int
    min_value: int
    max_value: int


class RandFloats(BaseModel):
    values: List[float]
    min_value: float
    max_value: float
    seed: Union[float, str, int]
    quantity: int
