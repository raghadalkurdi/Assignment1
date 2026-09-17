#5. Days of the Week
# Create a tuple containing the seven days of the week
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# 1. Print the entire tuple
print("1. Entire tuple:", days_of_week)

# 2. Print the first day
print("2. First day:", days_of_week[0])

# 3. Print the last day
print("3. Last day:", days_of_week[-1])

# 4. Attempt to change one of the values (This will cause an error)
try:
    days_of_week[0] = "Funday"
except TypeError as e:
    print("4. Attempted change result:", e)
    print("   Explanation: Tuples are immutable. You cannot reassign, add, or remove items after creation.")