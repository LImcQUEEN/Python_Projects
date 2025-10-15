arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def BubbleSort(): # no parameter unless asked by examiner
    for x in range(0, 10):
        for y in range(0, 9): # value of y is one less then x as we make pair of element
            if arrayData[y]>arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

BubbleSort()
print(arrayData)