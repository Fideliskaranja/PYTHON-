print("Try programiz.pro")

# Define the students' heights
students = {
    "John": 170,
    "Alice": 172,
    "Bob": 150
}
def find_tallest_student(students):
    
    tallest_student = max(students, key=students.get)
    return tallest_student

tallest_student = find_tallest_student(students)
print(f"{tallest_student} is the tallest")

for student, height in students.items():
    print(f"{student}: {height}cm")
    