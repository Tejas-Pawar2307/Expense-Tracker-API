from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ExpenseCreateDTO(BaseModel):
    title : str
    amount : float
    category : Optional[str] = None
    