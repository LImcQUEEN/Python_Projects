import mymodule
Names = [""] * 5
stack_pointer = 0


def Push(element):
    global Names
    global stack_pointer
    if stack_pointer > 4:
        print("Stack Full")
    else:
        Names[stack_pointer] = element
        stack_pointer = stack_pointer + 1


def Pop():
    global Names
    global stack_pointer
    if stack_pointer == 0:
        print("Stack Empty")
    else:
        stack_pointer = stack_pointer - 1
        print(Names[stack_pointer])


def PrintStack():
    global Names
    global stack_pointer
    print(stack_pointer)
    for x in range(0, len(Names)):
        print(Names[x])


Push("Ali")
Push("Ahmed")
Push("Taha")
Push("Muhammad")
Push("Khan")
Pop()
Push("Salman")
PrintStack()

