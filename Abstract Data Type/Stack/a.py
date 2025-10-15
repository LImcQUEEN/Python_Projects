# DECLARE StackData : ARRAY [0:9] OF INTEGER
# Question part a
global StackData
global stack_pointer
StackData = [0] * 10
stack_pointer = 0
# Question part b


def printstack():
    global StackData
    global stack_pointer
    print(stack_pointer)
    for x in range(0, 10):
        print(StackData[x])
# Question part c

def push(number):
    global stack_pointer
    global StackData
    if stack_pointer > 9:
        return False
    else:
        StackData[stack_pointer] = number
        stack_pointer = stack_pointer + 1
        return True

for x in range(0, 11):
    user_num = int(input("Please enter a number: "))
    temp = push(user_num)
    if temp == False:
        print("Can't Add More Numbers")
    else:
        print("Value Successfully Added")
printstack()


def Pop():
    global StackData
    global stack_pointer
    if stack_pointer == 0:
        return -1
    else:
        stack_pointer = stack_pointer - 1
        return StackData[stack_pointer]

