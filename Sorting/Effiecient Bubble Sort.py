arrayData = [1, 5, 6, 7, 8, 10, 12, 13, 15, 21]


def bubblesort():
    noswaps = False
    boundary = 9
    outercount = 0
    innercount = 0
    while noswaps == False:
        noswaps = True
        for y in range(0, boundary):
            if arrayData[y] > arrayData[y+1]: # for ascending sign is > and for decensing is <
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
                noswaps = False
            innercount = innercount + 1
        boundary = boundary - 1
        outercount = outercount +1
    print(innercount, "Inner")
    print(outercount, "Outer")

bubblesort()
print(arrayData)
