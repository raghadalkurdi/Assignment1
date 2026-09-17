# ==============================================================================
# STUDENT INFORMATION MANAGER
# ==============================================================================

# 1. Basic Variables
student_name = "Raghad"        # String
student_age = 22                # Integer
student_height = 168.0          # Float (in cm)
is_enrolled = True              # Boolean

print("=== BASIC VARIABLES ===")
print("Name:", student_name)
print("Age:", student_age)
print("Height:", student_height, "cm")
print("Currently Enrolled:", is_enrolled)
print("\n" + "="*50 + "\n")


# 2. List Operations
skills = ["Python", "PHP", "Laravel", "HTML", "SQL"]

print("=== LIST OPERATIONS ===")
# Print the first item
print("1. First skill:", skills[0])

# Add a new item
skills.append("Git")
print("2. Added 'Git':", skills)

# Remove one item
skills.remove("HTML")
print("3. Removed 'HTML':", skills)

# Print the updated list
print("4. Final updated list:", skills)
print("\n" + "="*50 + "\n")


# 3. Tuple Operations
favorite_numbers = (7, 14, 21)

print("=== TUPLE OPERATIONS ===")
# Print the second number (index 1)
print("Second favorite number:", favorite_numbers[1])
print("\n" + "="*50 + "\n")


# 4. Set Operations
# Including "Pilates" as a duplicate value
hobbies = {"Pilates", "Reading", "Cycling", "Pilates"}

print("=== SET OPERATIONS ===")
# Print the set
print("1. Initial Set:", hobbies)

# Explanation output
print("2. Explanation: The duplicate value 'Pilates' was automatically removed because sets only store unique elements.")

# Add a new hobby
hobbies.add("Swimming")
print("3. Set after adding 'Swimming':", hobbies)
print("\n" + "="*50 + "\n")


# 5. Dictionary Operations
student_info = {
    "name": student_name,
    "age": student_age,
    "height": student_height,
    "is_enrolled": is_enrolled,
    "skills": skills,
    "favorite_numbers": favorite_numbers,
    "hobbies": hobbies
}

print("=== DICTIONARY OPERATIONS ===")
# Print the student's name
print("1. Name:", student_info["name"])

# Print their skills
print("2. Skills:", student_info["skills"])

# Add a new key called "country"
student_info["country"] = "Malaysia"
print("3. Added 'country' key.")

# Update the student's age
student_info["age"] = 23
print("4. Updated age to 23.")

# Print the complete dictionary
print("5. Complete Dictionary:")
print(student_info)