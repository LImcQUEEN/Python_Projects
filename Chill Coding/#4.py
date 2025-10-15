array = [""]*5
head_pointer = -1
tail_pointer = 0


def Enqueue(element_p):
    global head_pointer
    global tail_pointer
    global array
    if tail_pointer > len(array)-1:
        print("Queue is Full")
    else:
        array[tail_pointer] = element_p
        tail_pointer = tail_pointer + 1
        if head_pointer == -1:
            head_pointer = 0


def Dequeue():
    global head_pointer
    global tail_pointer
    global array
    if head_pointer == -1:
        print("Queue is Empty")
    else:
        item = array[head_pointer]
        print(item)
        head_pointer = head_pointer + 1
    if head_pointer == tail_pointer:
        head_pointer = -1
        tail_pointer = 0


Enqueue("Ahmed")
Enqueue("Aryan")
Enqueue("Danish")
Enqueue("Lex")
Enqueue("Tom")
Dequeue()
Dequeue()
Enqueue("Aliya")
print(array)