def recursion(x):
    y = x * 2
    if y < 10:
        recursion(y)
        print(y)


recursion(4)