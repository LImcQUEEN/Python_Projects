# DECLARE Numbers : ARRAY[0:4]OF INTEGER
Numbers = [0] * 5
start_pointer = -1
end_pointer = 0


def dequeue():
    global Numbers
    global start_pointer
    global end_pointer
    if start_pointer == -1:
        print("Queue Is Empty")
    else:
        print(Numbers[start_pointer])
        start_pointer = start_pointer + 1

    if start_pointer == end_pointer:
        start_pointer = -1
        end_pointer = 0
