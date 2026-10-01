from dataclasses import dataclass, field
@dataclass
class Expense: 
    expense_name : str
    cost : float
    category : str
    date : str
    id : int