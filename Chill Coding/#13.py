arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def linearSearch(number):
    for x in range(0, 10):
        if arrayData[x] == number:
            print(f"Element found at index {x}")


def binarySearch(number):
    upperBound = 9
    lowerBound = 0
    valueFound = False
    notInList = False

    while not valueFound and not notInList:
        midpoint = int((upperBound+lowerBound)/2)

        if arrayData[midpoint] == number:
            valueFound = True
            return True
        elif number > arrayData[midpoint]:
            lowerBound = midpoint + 1
        else:
            upperBound = midpoint - 1
        if lowerBound > upperBound:
            notInList = True
            return False



