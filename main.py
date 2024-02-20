from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory storage
students = {}


class Student:
    def __init__(self, id, name, age, sex, height):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height


@app.post("/students/")
def create_student(id: int, name: str, age: int, sex: str, height: float):
    if id in students:
        raise HTTPException(status_code=400, detail="Student with this id already exists")
    student = Student(id=id, name=name, age=age, sex=sex, height=height)
    students[id] = student
    return student


@app.get("/students/{student_id}")
def read_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.get("/students/")
def read_students():
    return list(students.values())


@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, sex: str, height: float):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    student = students[student_id]
    student.name = name
    student.age = age
    student.sex = sex
    student.height = height
    return student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": "Student deleted"}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Student API"}
