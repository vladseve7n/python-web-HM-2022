from pydantic import BaseModel


class RandInt(BaseModel):
    value: int
    min_value: int
    max_value: int
