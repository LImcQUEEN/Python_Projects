# DECLARE Queue : ARRAY [0:9] OF INTEGER
Queue = [0]*10
front_pointer = -1
rear_pointer = 0


def Linear_Enqueue(element_p):
    global Queue
    global front_pointer
    global rear_pointer
    if rear_pointer < 9:
        Queue[rear_pointer] = element_p
        rear_pointer = rear_pointer + 1
        if front_pointer == -1:
            front_pointer = 0
    else:
        print("Queue is Full! ")


def Linear_Dequeue():
    global Queue
    global front_pointer
    global rear_pointer
    if front_pointer == -1:
        print("Queue is Empty! ")
    else:
        temp = Queue[front_pointer]
        print(temp)
        front_pointer = front_pointer + 1
    if front_pointer == rear_pointer:
        front_pointer = -1
        rear_pointer = 0


Linear_Enqueue(1)
Linear_Enqueue(3)
Linear_Enqueue(4)
Linear_Enqueue(6)
Linear_Enqueue(71)
Linear_Enqueue(19)
Linear_Enqueue(23)
Linear_Enqueue(56)
Linear_Enqueue(45)
Linear_Dequeue()
print(Queue)