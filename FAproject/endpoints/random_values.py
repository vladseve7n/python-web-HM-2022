from fastapi import APIRouter, Query
import random
from models.random_values import RandInt

router = APIRouter()


@router.get('/getRandomInt', response_model=RandInt)
async def get_random(min_value: int = Query(0, description='Min value of generated integer'),
                     max_value: int = Query(255, description='Max value of generated integer')):
    value = random.randint(a=min_value, b=max_value)
    return RandInt(value=value,
                   min_value=min_value,
                   max_value=max_value)
