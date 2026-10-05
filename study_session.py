from dataclasses import dataclass
from datetime import date

@dataclass
class StudySession:
    day:date
    minutes:int
    topic:str
    
         
         
    def __post_init__(self):
        if self.minutes <= 0:
            raise ValueError("minutes cannot be less than 0")
        elif self.topic.strip() == "" or self.topic == " ":
            raise ValueError("the topic cannot be empty")
        

try:
    session1 = StudySession(date(2026, 9, 1), 0, "Math")
    print("Created :",session1)
except ValueError as e:
    print("Error:", e)  # Output: minutes cannot be less than 0

try:
    session2 = StudySession(date(2026, 9, 2), 30, " ")
    print("Created :",session2)
except ValueError as e:
    print("Error:", e)

try:
    session3 = StudySession(date(2026, 9, 3),45,"python")
    print("Created :",session3)
except ValueError as e:
    print("Error:", e)

try:
    session4 = StudySession(date(2026, 9, 4), 60, "   ")
    print("Created :",session4)
except ValueError as e:
    print("Error:", e)
        
