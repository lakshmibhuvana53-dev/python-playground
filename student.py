import json
import student
student_data = [{
    "name": "John Doe",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science", "History"]
}, 
{
    "name": "Jane Smith",
    "age": 22,
    "grade": "B",
    "courses": ["English", "Art", "Biology"]
},
{
    "name": "Alice Johnson",
    "age": 19,
    "grade": "A",
    "courses": ["Math", "Physics", "Chemistry"]
}]
with open('student.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(type(data[0]))




