#Part 4: Sets

#6. Remove Duplicate Values
numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1]

# 1. Convert the list into a set
unique_numbers = set(numbers)

# 2. Print the result
print("1. Original list:", numbers)
print("2. Set result:", unique_numbers)




#7. Unique Programming Languages
languages_list = ["Python", "Java", "Python", "C++", "JavaScript", "Python"]

# 1. Convert the list into a set to get unique languages
languages_set = set(languages_list)
print("1. Unique programming languages set:", languages_set)

# 2. Add "Django" to the set
languages_set.add("Django")
print("2. Set after adding 'Django':", languages_set)