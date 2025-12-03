a = input("Enter some full number to write: ")
try:
    a = int(a)
    print(f'{a} is a valid number.')
except ValueError:
    print(f'{a} is not a valid number and it is a string')
