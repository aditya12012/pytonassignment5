# Task 1: Create a Dictionary of Student Marks

# Step 1: Create a dictionary with student names and marks
student_marks = {
    "Aditya": 85,
    "Saina": 92,
    "Rohan": 76,
    "Priya": 89,
    "Amit": 95
}

# Step 2: Ask the user to input a student's name
name = input("Enter student name: ")

# Step 3: Check if the student exists in the dictionary
if name in student_marks:
    print(f"Marks of {name}: {student_marks[name]}")
else:
    print("Student not found in the record.")
