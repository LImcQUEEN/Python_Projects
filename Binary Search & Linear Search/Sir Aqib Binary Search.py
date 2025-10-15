arrayData = [1, 5, 6, 7, 8, 10, 12, 13, 15, 21]
def BinarySearch(number):
    count = 0
    upperbound = 9
    lowerbound = 0
    valuefound = False
    while valuefound == False and upperbound<lowerbound:
        midpoint = int((upperbound + lowerbound)/2)
        if number == arrayData[midpoint] :
            valuefound = True
            return True
        elif number > arrayData[midpoint]:
            lowerbound = midpoint + 1
        elif number < arrayData[midpoint]:
            upperbound = midpoint - 1
            count = count + 1
search = BinarySearch(6)
if search == True:
    print("Number Found")
