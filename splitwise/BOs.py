import dataclasses
from typing import List, Any, Optional

@dataclasses.dataclass
class UserBO:
    name: str
    email: str
    uid: int
    phoneNumber: str


@dataclasses.dataclass
class ExpenseItemBO:
    payer: Any
    amount: int
    splitStrategy: str
    paidForUsers:  List[Any]
    name: Optional[Any] = ""
    notes: Optional[Any] = ""
    paidPercents:  Optional[List] = dataclasses.field(default_factory=list)
    paidAmounts:  Optional[List] = dataclasses.field(default_factory=list)
    images: Optional[List] = dataclasses.field(default_factory=list)
