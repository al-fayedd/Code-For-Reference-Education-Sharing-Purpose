# Define a function called greet_user that
# Takes one argument, name.
# Prints a greeting message that includes the name.
def greet_user(name):
    print(f"Hello, {name}!")
greet_user("Jane")


# Modify the greet_user function:
# Add a second optional argument, greeting, with a default value of "Hello".
# The function should print the greeting followed by the name.
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user("Jane")
greet_user("Jane", "Good morning")

# Create a function sum_numbers that:
# Takes two arguments, a and b.
# Returns the sum of a and b.
def sum_numbers(a, b):
    return a + b
print(sum_numbers(1, 2))

#  Work with the following list: fruits = ["apple", "banana", "cherry", "date"].
# Perform the following operations:
# Add "elderberry" to the end of the list.
# Remove "banana" from the list.
# Insert "blueberry" at the second position in the list.
# Sort the list in alphabetical order.

fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.remove("banana")
fruits.insert(1, "blueberry")
fruits.sort()
print(fruits)

# Write a loop that:
# Prints numbers from 1 to 10.
# Stops the loop if the number is 7 (use the break statement).
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# Write a loop that:
# Prints numbers from 1 to 10.
# Skips the numbers that are multiples of 3 (use the continue statement).
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
