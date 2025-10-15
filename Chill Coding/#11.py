def table(x):
    y = x * 2
    if y < 100:
        table(y)
        print(y)


table(2)