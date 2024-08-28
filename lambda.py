# add = lambda x,y: x+y
# sub = lambda x,y: x-y
# mul = lambda x,y: x*y
# div = lambda x,y: x/y
# mod = lambda x,y: x%y
# exp = lambda x,y: x**y
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# print("5.Modulus")
# print("6.Exponent")

# Define a list of numbers

numbers = [1, 2, 3, 4, 5]
# Use the map function to apply a lambda function that squares each number in the list
# The lambda function takes each element 'x' from the list 'numbers' and returns 'x' squared (x **
# 2)
squared_numbers = list(map(lambda x: x ** 2, numbers))
# Print the list of squared numbers
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

words = ['apple', 'banana', 'cherry']
uppercase_words = list(map(lambda word: word.upper(), words))
print(uppercase_words) # Output: ['APPLE', 'BANANA', 'CHERRY']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # Output: [2, 4, 6, 8, 10]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers) # Output: [1, 3, 5, 7, 9]


