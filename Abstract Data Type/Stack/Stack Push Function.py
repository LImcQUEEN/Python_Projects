# DECLARE Names : ARRAY[0:4] OF STRING
Names = [""]*5
stack_pointer = 0


def push(value):
    global stack_pointer  # We want to use the actual value of stackpointer
    global Names        # there will be change in array so global is used

    if stack_pointer > 4:   # when the stack is full the pointer is outside the array
        print("Stack is full")
    else:
        Names[stack_pointer] = value
        stack_pointer = stack_pointer + 1   # we increment after adding
        # because first we need to add data then place pointer
        # in the next free space
        # however if examiner has initialized pointer value to
        # -1 then first we add then add data
