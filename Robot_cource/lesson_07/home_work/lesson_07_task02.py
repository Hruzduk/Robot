my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_generator():
    for i in my_list:
        yield i ** i

for i in my_generator():
    print(i)