#Part 5: Dictionaries
#8. Student Profile
student = {
    "Name": "Karam",
    "Age": 22,
    "Course": "Information Technology",
    "Level": "Undergraduate",
    "Skills": ["PHP", "Laravel", "Python"]
}

# 1. Print the entire dictionary
print("1. Entire dictionary:")
print(student)
print()

# 2. Print the student's name
print("2. Student's Name:", student["Name"])
print()

# 3. Add a new key called email
student["email"] = "karam@example.com"
print("3. Added email key:")
print(student)
print()

# 4. Change the student's level
student["Level"] = "Graduate"
print("4. Changed level to Graduate:")
print(student)
print()

# 5. Remove the age key
del student["Age"]  
print("5. Removed Age key:")
print(student)
print()

# 6. Print the final dictionary
print("6. Final dictionary:")
print(student)