class Node:
    # DECLARE Pointer : INTEGER
    # DECLARE Data : INTEGER
    def __init__(self, data_p, pointer_p):
        self.Pointer = pointer_p
        self.Data = data_p


# DECLARE linkedList : ARRAY [0:9] OF NODE
linkedList = [Node(1, 1),      #index-0
              Node(5, 4),      #index-1
              Node(6, 7),      #index-2
              Node(7, -1),             #index-3
              Node(2, 2),     #index-4
              Node(0, 6),     #index-5
              Node(0, 8),     #index-6
              Node(56, 3),   #index-7
              Node(0, 9),    #index-8
              Node(0, -1)]           #index-9
start_pointer = 0
empty_list = 5  # points to the first empty index in array


def addNode(current_pointer):
    global linkedList
    global empty_list
    data = int(input("Enter the Data to Add:"))
    # check if array is full or not
    if empty_list < 0 or empty_list > 9:
        return False
    else:
        freelist = empty_list
        empty_list = linkedList[empty_list].Pointer
        newNode = Node(data, -1)
        linkedList[freelist] = newNode
        previous_pointer = 0
        while current_pointer != 0:
            previous_pointer = current_pointer
            current_pointer = linkedList[current_pointer].Pointer
        linkedList[previous_pointer].Pointer = freelist
        return True


def deleteNode():
    global linkedList
    global empty_list
    global start_pointer
    current_pointer = start_pointer
    delete_data = input("Enter the data to delete")
    previous_pointer = 0
    while current_pointer != -1 and linkedList[current_pointer] != delete_data:
        previous_pointer = current_pointer
        current_pointer = linkedList[current_pointer].Pointer
    if current_pointer == -1:
        print("Node not part of Linked List")
    else:
        if current_pointer == start_pointer:
            start_pointer = linkedList[current_pointer].Pointer
        else:
            linkedList[previous_pointer].Pointer = linkedList[current_pointer].Pointer

        linkedList[current_pointer].Data = 0
        linkedList[current_pointer].Pointer = empty_list
        empty_list = current_pointer


def outputNodes():
    global start_pointer
    global linkedList
    current_pointer = start_pointer
    while current_pointer != -1:
        print(linkedList[current_pointer].Data)
        current_pointer = linkedList[current_pointer].Pointer


def searchNodes(search_data):
    global linkedList
    global start_pointer
    current_pointer = start_pointer
    while current_pointer != -1:
        if linkedList[current_pointer].Data == search_data:
            return current_pointer
        else:
            current_pointer = linkedList[current_pointer].Pointer
    current_pointer = -1
    return current_pointer


temp = searchNodes(1)
if temp == -1:
    print("Element not Found ")
else:
    print(f"Element found at index {temp}")