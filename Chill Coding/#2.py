# DECLARE Names : ARRAY[0:4] OF STRING
Names = [""] * 5
start_pointer = -1
end_pointer = 0


def Enqueue(element_p):
    global Names
    global start_pointer
    global end_pointer
    if end_pointer < 5:
        Names[end_pointer] = element_p
        end_pointer = end_pointer + 1

        if start_pointer == -1:
            start_pointer = 0

    else:
        print("Queue is Full")


def Dequeue():  # The Value is never deleted rather
    # Ignored and when new value come
    # We place that value in that place
    global Names
    global start_pointer
    global end_pointer
    if start_pointer == -1:
        print("Queue is Full")
    else:
        temp = Names[start_pointer]
        print(temp)
        start_pointer = start_pointer + 1
    if start_pointer == end_pointer:
        start_pointer = -1
        end_pointer = 0


Enqueue("Ahmed")
Enqueue("Moin")
Enqueue("Sarwar")
Enqueue("Ruqqaiya")
Dequeue()
Enqueue("Shabana")
Enqueue("Shabnum")