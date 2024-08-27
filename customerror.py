# #raising custom error

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     if b == 0:
#         raise ZeroDivisionError
#     print(a/b)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")


# a = int(input("Enter a number: "))
# if a < 0:
#     raise ValueError("That's not a positive number!")
# print(a)

# def check_positive_number():
#     a = int(input("Enter a number: "))
#     if a < 0:
#         raise ValueError("That's not a positive number!")
#     return(a)

# check_positive_number()

def check_positive_number(a):
    # Semak jika nombor adalah negatif
    if a < 0:
        raise ValueError("Itu bukan nombor positif!")
    return a

try:
    # Panggil fungsi dengan nombor positif
    print(check_positive_number(-5))
except ValueError as ve:
    # Tangkap dan cetak mesej ralat jika berlaku
    print(ve)
