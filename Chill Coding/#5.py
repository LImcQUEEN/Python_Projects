Array = [""]*5
head_pointer = 0
tail_pointer = 0
number_items = 0


def Enqueue(element_p):
    global Array
    global head_pointer
    global tail_pointer
    global number_items
    if number_items == len(Array):
        return False
    Array[tail_pointer] = element_p
    if tail_pointer >= len(Array) - 1:
        tail_pointer = 0
    else:
        tail_pointer = tail_pointer + 1
    number_items = number_items + 1
    return True


def Dequeue():
    global Array
    global head_pointer
    global tail_pointer
    global number_items
    if number_items == 0:
        print("Queue is Empty")
    else:
        value = Array[head_pointer]
        head_pointer = head_pointer + 1
        if head_pointer > len(Array)-1:
            head_pointer = 0
        number_items = number_items -1
        print(value)


Enqueue("A")
Enqueue("B")
Enqueue("C")
Enqueue("D")
Enqueue("E")
Dequeue()
Enqueue("F")
print(Array)