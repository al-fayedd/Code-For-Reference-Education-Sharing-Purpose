counter = 0

def increment_counter():
    global counter
    counter += 1
    print(counter)

def reset_counter():
    counter = 0
    print(counter)

increment_counter()
increment_counter()
increment_counter()
reset_counter()
print(counter)

import os # Operating System

print(os.getcwd())
print(os.listdir())

os.mkdir("test_dir")

os.chdir("test_dir")

print(os.getcwd())

with open("test_file.txt", "w") as file:
    file.write("This is a test file.")

os.remove("test_file.txt")

os.rmdir("test_dir")


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    finally:
        print("Division operation completed")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

try:
    result = divide_numbers(a, b)
    print(f"{a} / {b} = {result}")
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
finally:
    print("End of program")
