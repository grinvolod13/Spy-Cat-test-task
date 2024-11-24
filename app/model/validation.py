from pydantic import BaseModel, RootModel
from annotated_types import Len
from typing import List, Annotated

class Target(BaseModel):
    ...

class Targets(RootModel):
    root: Annotated[List[Target], Len(1, 3)]
