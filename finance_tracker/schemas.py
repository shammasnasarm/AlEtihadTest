from datetime import datetime
from typing import Optional
from pydantic import BaseModel, model_validator


class Transaction(BaseModel):
    date: datetime
    description: str
    amount: float
    type: str = ""
    category: Optional[str] = None


    @model_validator(mode="after")
    def set_type(self) -> "Transaction":
        self.type = "income" if self.amount > 0 else "expense"
        return self
