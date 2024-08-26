#Task 1
# # Creating Tuples
fruits = ("apple", "banana", "cherry", "date")
print(fruits[0], fruits[-1])

# Tuple Operations
numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers
print(a, b, rest)

# Tuple Immutability
try:
    fruits[1] = "blueberry"
except TypeError:
    print("Tuples are immutable, cannot change the second element of the fruits tuple to 'blueberry'.")


#Task 2
# Creating Sets
colors = {"red", "green", "blue", "yellow"}
colors.add("purple")
colors.add("black")
print("Colors:", colors)

# Set Operations
primary_colors = {"red", "blue", "yellow"}
print("Intersection:", colors.intersection(primary_colors))
print("Union:", colors.union(primary_colors))
print("Difference:", colors.difference(primary_colors))

# Set Membership
print("Is 'green' in primary_colors?", "green" in primary_colors)
print("Is 'orange' not in colors?", "orange" not in colors)


#Task 3
# Creating Dictionaries
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}

print("Bob's grade:", student_grades["Bob"])


# Dictionary Operations
student_grades["Eve"] = 88
student_grades["Alice"] = 95
del student_grades["Charlie"]

print("Updated student grades:", student_grades)


# Looping Through a Dictionary
for name, grade in student_grades.items():
    print(f"Student: {name}, Grade: {grade}")
