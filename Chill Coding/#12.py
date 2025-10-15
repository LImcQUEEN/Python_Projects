Students = [10, 30, 12, 213, 230, 32103]


def BinarySearch():
    global Students
    upperbound = 0
    lowerbound = 4
    searchedValue = int(input("enter number you want to search: "))
    found = False
    notInArray = False
    while not found and not notInArray:
        midValue = int((upperbound+lowerbound)/2)
        if searchedValue == midValue:
            found = True
        elif searchedValue > midValue:
            lowerbound = midValue + 1
        elif searchedValue < midValue:
            upperbound = midValue - 1
        elif lowerbound > upperbound:
            notInArray = True