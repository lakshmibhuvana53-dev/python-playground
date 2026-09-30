from dataclasses import dataclass, field
@dataclass
class Expense:
    id : int 
    expense_name : str
    cost : float
    category : str
    date : str
