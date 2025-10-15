def printArray():
    try:
        newNum = int(input("Enter any number: "))
        result = newNum + 100
        print(result)
    except ValueError:  # Only deal with datatype errors
        print("Invalid Input please input a number")


def readFile():
    try:
        newFile = open("Score.txt", "r")    # There is no such file existing in directory
        temp = newFile.readline()   # Which will cause and exception
        print(temp)
    except IOError:  # Only deal with file error
        print("File doesn't exist in the directory")


def Division():
    try:
        number = int(input("Enter Any Number: "))   # If user input Alphabet causing an exception
        divisor = 0
        result = number / divisor   # Division by zero
        print(result)   # causing an exception
    except ZeroDivisionError:   # Only deal with zero division error
        print("Division by zero")