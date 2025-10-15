# DECLARE QueueArray : ARRAY [0:9] OF STRING
head_pointer = 0
tail_pointer = 0
number_items = 0    # Tells that the queue is full or not
QueueArray = [""]*10
#   Cannot pass parameter as Byref so declare them as global


def enqueue(data):
    global head_pointer
    global tail_pointer
    global number_items
    global QueueArray
    if number_items == 10:
        return False
    QueueArray[tail_pointer] = data
    if tail_pointer >= 9:  # As soon as tail_pointer at max index then
        tail_pointer = 0   # roll it back to 0 index position
# for enqueue use tail_pointer and for dequeue use head_pointer
    else:
        tail_pointer = tail_pointer + 1
    number_items = number_items + 1
    return True
