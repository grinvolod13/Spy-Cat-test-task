from fastapi import Depends
from pydantic import BaseModel, RootModel, Field, field_validator
from pydantic import Field
from annotated_types import Len, Ge
from typing import List, Annotated, Optional

from app.const import CAT_BREED_API

class Target(BaseModel):
    name: str
    country: str

class UpdatedTarget(BaseModel):
    name: str
    country: str
    notes: str = ""
    complete: bool = False
    
class Mission(BaseModel):
    id: int
    cat: Optional['Cat']
    targets: 'UpdatedTargets' = Field(default_factory=list)
    complete: bool



class Targets(RootModel):
    root: Annotated[List[Target], Len(1, 3)]
    
class UpdatedTargets(RootModel):
    root: Annotated[List[UpdatedTarget], Len(1, 3)]
    
Salary = Annotated[float, Ge(0)]


class Cat(BaseModel):
    name: str
    years_of_experience: Annotated[float, Ge(0)] # i belive number like 1.5 yrs should be valid in CVs
    breed: str
    salary: Salary
    mission: list
    class Config:
        from_attributes = True

import aiohttp

async def get_breeds_set()-> set[str]:
    """lowercase breeds set"""
    async with aiohttp.ClientSession() as session:
        async with session.get(CAT_BREED_API) as r:
            json_r = await r.json()
            breeds: set[str] = {breed['name'].lower() for breed in json_r}
            return breeds
            
# external from pydantic validation, because validation model shouldn't be IO bounded 
async def validate_breed(cat: Cat) -> bool:
    breeds = await get_breeds_set()
    cat.breed = cat.breed.lower()
    return (cat.breed in breeds)
    
    