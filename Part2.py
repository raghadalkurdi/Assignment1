
#3. Favourite Foods
favorite_foods = [
    "Chicken",
    "Greek Yogurt",
    "Pizza",
    "Noodles",
    "Wedges",
]
# Print the entire list
print("Favourite Foods list:", favorite_foods)
# Print the first and last food  
print(f"First food: {favorite_foods[0]} | Last food: {favorite_foods[-1]}")
# Add one more food
favorite_foods.append("Cake")
print("Adding cake to Favourite Foods list:", favorite_foods)
#Remove one food
favorite_foods.remove("Pizza")
print("After removing Pizza:", favorite_foods)
#Change one food to another food
favorite_foods[2] = "Pie"
print("After modifying a food:", favorite_foods)
# Print the final list
print("Final list:", favorite_foods)



#4. Student Scores
# Initial list of scores
scores = [75, 80, 65, 90, 85]

# 1. Print all the scores
print("1. All scores:", scores)

# 2. Print the highest score
highest_score = max(scores)
print("2. Highest score:", highest_score)

# 3. Print the lowest score
lowest_score = min(scores)
print("3. Lowest score:", lowest_score)

# 4. Add a new score of 95
scores.append(95)
print("4. Added new score: 95")

# 5. Print the updated list
print("5. Updated scores list:", scores)
