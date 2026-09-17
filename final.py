#Final Challenge
#9. Student Management Data
# Create a dictionary containing information for 3 students
students = {
    "student1": {
        "name": "John",
        "age": 22,
        "course": "Backend Development",
        "skills": ["Python", "HTML", "Git"]
    },
    "student2": {
        "name": "Mary",
        "age": 24,
        "course": "Data Analysis",
        "skills": ["Excel", "SQL", "Python"]
    },
    "student3": {
        "name": "Raghad",
        "age": 22,
        "course": "Full-Stack Development",
        "skills": ["PHP", "Laravel", "Python"]
    }
}

# Iterate through the dictionary and print each student's information
for student_id, details in students.items():
    print(f"--- {student_id.upper()} ---")
    print(f"Name: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"Course: {details['course']}")
    print(f"Skills: {', '.join(details['skills'])}\n")