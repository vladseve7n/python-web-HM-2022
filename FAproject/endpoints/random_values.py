from typing import Union

from fastapi import APIRouter, Query, Path, HTTPException, Body
import random
from models.random_values import RandInt, RandFloats

router = APIRouter()


@router.get('/getRandomInt', response_model=RandInt)
async def get_random_int(min_value: int = Query(0, description='Min value of generated integer'),
                         max_value: int = Query(255, description='Max value of generated integer')) -> RandInt:
    value = random.randint(a=min_value, b=max_value)
    return RandInt(value=value,
                   min_value=min_value,
                   max_value=max_value)


@router.get('/getRandomIntBySeed/{seed}', response_model=RandInt)
async def get_random_int_by_seed(min_value: int = Query(0, description='Min value of generated integer'),
                                 max_value: int = Query(255, description='Max value of generated integer'),
                                 seed: Union[int, str, float] = Path(..., description='Random seed for '
                                                                                      'generate value')) -> RandInt:
    random.seed(seed)
    return await get_random_int(min_value, max_value)


@router.post('/getRandomFloat', response_model=RandFloats)
async def get_random_float(min_value: float = Body(0, description='Min value of generated float values'),
                           max_value: float = Body(255, description='Max value of generated float values'),
                           seed: Union[float, str, int] = Body(42, description='Random seed for generate value'),
                           quantity: int = Body(5, description='The quantity of values to generate')) -> RandFloats:
    random.seed(seed)
    return RandFloats(values=[random.uniform(a=min_value, b=max_value) for _ in range(quantity)],
                      min_value=min_value,
                      max_value=max_value,
                      quantity=quantity,
                      seed=seed
                      )
