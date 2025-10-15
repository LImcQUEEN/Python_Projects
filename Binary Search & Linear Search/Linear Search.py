#DECLARE arrayData : ARRAY[0 : 9] OF INTEGER
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(number):
    for x in range(0, 10): #Uptill 10 but not including 10

        if arrayData[x] == number:
            return True
    return False
linearSearch(15)
value= int(input("Enter A Number: "))
found = linearSearch(value)

if found == True:
    print("Your Searched Number Was Found")
else:
    print("Your Number Wasn't Found")

