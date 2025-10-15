# DECLARE Numbers : ARRAY[0:4]OF INTEGER
Numbers = [0] * 5
start_pointer = -1
end_pointer = 0


def enqueue(number):
    global Numbers
    global start_pointer
    global end_pointer
    if end_pointer < 4:
        Numbers[end_pointer] = number
        end_pointer = end_pointer + 1
        if start_pointer == -1:
            start_pointer = 0
    else:
        print("Queue is Full")
