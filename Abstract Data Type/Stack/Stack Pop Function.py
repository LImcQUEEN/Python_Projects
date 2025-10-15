# DECLARE Names : ARRAY[0:4] OF STRING
Names = [""]*5
stack_pointer = 0


def pop():
    global Names
    global stack_pointer
    if stack_pointer == 0:
        print("Empty Stack")
    else:
        stack_pointer = stack_pointer - 1
        print(Names[stack_pointer])     # Show the value that's removed
        Names[stack_pointer] = ""


pop()
