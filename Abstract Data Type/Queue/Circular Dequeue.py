# DECLARE QueueArray : ARRAY [0:9] OF STRING
head_pointer = 0
tail_pointer = 0
number_items = 0    # Tells that the queue is full or not
QueueArray = [""]*10
#   Cannot pass parameter as Byref so declare them as global


def dequeue():
    global head_pointer
    global tail_pointer
    global number_items
    global QueueArray

    if number_items == 0:
        return False
    else:
        value = QueueArray[head_pointer]
        head_pointer = head_pointer + 1

        if head_pointer > 9:  # This is the concept of circular queue
            head_pointer = 0  # If dequeue then head_pointer is cycled

        number_items = number_items - 1
        return value
