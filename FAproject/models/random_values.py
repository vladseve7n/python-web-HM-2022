from pydantic import BaseModel
from typing import Optional


class RandInt(BaseModel):
    value: int
    min_value: int
    max_value: int

