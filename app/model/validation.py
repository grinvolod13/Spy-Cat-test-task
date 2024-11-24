from pydantic import BaseModel
from annotated_types import Len
from typing import List, Annotated

class Target(BaseModel):
    ...

Targets = Annotated[List[Target], Len(1, 3)]