
from typing import Any
import dataclasses

@dataclasses.dataclass
class VehicleBO:
    color: str
    registration: str

@dataclasses.dataclass
class SlotBO:
    number: int
    is_vacant: bool = True
    vehicle : Any = None
