def sub(x, y):
    return x - y if x > y else 0

def mult(x, y):
    return x * y

def div(x, y):
    return x / y if y != 0 else 0

def pow(x, y):
    return x ** y

def rem(x, y):
    return x % y

def is_even(num):
    return True if num % 2 == 0 else False

def print_n(num):
    print("Inside print function")
    for x in range(1, num+ 1 ):
        if is_even(x):
            print(x)


if __name__ == "__main__":
    print(sub(10, 5))

    print(sub(5, 10))

    print(mult(2, 3))

    print(div(10, 5))

    print(div(10, 0))

    print(pow(2, 2))

    print(pow(3, 4))

    print(rem(5, 2))

    (print_n(51))

