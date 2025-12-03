def type_error(a, b):
    try :
        a = int(a)
        b = int(b)
        print(f'Sum {a} + {b}: ')
        print(a + b)
    except ValueError:
        print("Do not doing like this")
    else:
        print("No error occurred")



a = input(f'Enter a first number: ')
b = input(f'Enter a second number: ')
type_error(a, b)

