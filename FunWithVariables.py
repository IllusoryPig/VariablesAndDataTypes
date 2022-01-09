if __name__ == "__main__":
    a = 5
    b = 7
    c = a + b
    print(c)

print("Print greater number")

if __name__ == "__main__":
    a = 5
    b = 7
    if b > a:
        print(b)
    else:
        print(a)

print("Print greater number 3")

if __name__ == "__main__":
    a = 2
    b = 9
    c = 11
    if a > b and a > c:
        print (a)
    if b > a and b > c:
        print (b)
    if c > a and c > b:
        print (c)

print("Print greater number 3 cleaner way")

if __name__ == "__main__":
    a = 2
    b = 9
    c = 8
    if a > b and a > c:
        print (a)
    elif b > a and b > c:
        print (b)
    else:
        print (c)

print("Swap numbers")

if __name__ == "__main__":
    a = 5
    b = 7
    c = a
    a = b
    b = c

    print(a)
    print(b)
