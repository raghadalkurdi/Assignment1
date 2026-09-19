# a. Initial Setup & Batch Count
count = int(input("How many student entries do you want to create? "))
student_records = {}

# b. Dynamic Entry Loop
for i in range(count):
    print(f"--- Entry {i + 1} ---")
    name = input("Enter student name: ").strip()
    score = float(input("Enter score (0-100): "))
    student_records[name] = score

# Tracking variables for Class Summary
total_score = 0
passed_count = 0
failed_count = 0

# c. Evaluation & Performance Analysis
print("========================================")
print("EVALUATION RESULTS")
print("========================================")

for name, score in student_records.items():
    total_score += score

    # Determine grade and status using conditional checks
    if score >= 70:
        grade = "Grade A"
        status = "Passed with Distinction"
        passed_count += 1
    elif score >= 50:
        grade = "Grade B"
        status = "Passed"
        passed_count += 1
    else:
        grade = "Grade F"
        status = "Needs Improvement"
        failed_count += 1

    print(f"- {name}: Score {score:.1f} | {grade} | {status}")

# d. Class Summary
print("========================================")
print("CLASS PERFORMANCE")
print("========================================")

# Calculate class average safely (handling 0 students if count is 0)
average_score = (total_score / count) if count > 0 else 0.0

print(f"Average Score: {average_score:.1f}")
print(f"Total Passed: {passed_count}")
print(f"Total Failed: {failed_count}")