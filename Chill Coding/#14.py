number = [9, 10, 10, 23, 21]


def bubbleSort():
    noSwap = False
    boundary = len(number) - 1
    while not noSwap:
        noSwap = True
        for x in range(0, boundary):
            if number[x] > number[x+1]:
                temp = number[x]
                number[x] = number[x+1]
                number[x+1] = temp
                noSwap = True
        boundary = boundary - 1


def insertionSort():
    arraySize = 5
    for pointer in range(1, arraySize):
        valueInsert = number[pointer]
        holePosition = pointer
        while holePosition > 0 and number[holePosition-1] > valueInsert:
            number[holePosition-1] = number[holePosition]
            holePosition = holePosition - 1
        number[holePosition] = valueInsert


insertionSort()
print(number)
