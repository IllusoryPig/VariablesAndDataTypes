def sub(x, y):
    return x - y if x > y else 0


def mult(x, y):
    return x * y


def div(x, y):
    return x / y if y != 0 else 0


if __name__ == "__main__":
    print(sub(10, 5))

    print(sub(5, 10))

    print(mult(2, 3))

    print(div(10, 5))

    print(div(10, 0))
