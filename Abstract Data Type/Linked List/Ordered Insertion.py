class Node:
    # DECLARE data : INTEGER
    # DECLARE nextNode : INTEGER
    def __init__(self, data_p, nextNode_p):
        self.data = data_p
        self.nextNode = nextNode_p


# DECLARE linkedList : ARRAY [0:9] OF Node
linkedList = [
    Node(1, 1),
    Node(5, 4),
    Node(6, 7),
    Node(7, -1),
    Node(2, 2),
    Node(0, 6),
    Node(0, 8),
    Node(56, 3),
    Node(0, 9),
    Node(0, -1)
]
start_pointer = 0
empty_pointer = 5


def addNode():
    global linkedList
    global start_pointer
    global empty_pointer
    dataAdd = input("Enter Data to Add: ")
    if empty_pointer < 0 or empty_pointer > 9:
        return -1
    else:
        free_list = empty_pointer
        empty_pointer = linkedList[empty_pointer].nextNode
        newNode = Node(dataAdd, -1)
        linkedList[free_list] = newNode
        current_pointer = start_pointer
        previous_pointer = 0
        while current_pointer != -1 and linkedList[current_pointer].data < dataAdd:
            previous_pointer = current_pointer
            current_pointer = linkedList[current_pointer].nextNode

        if current_pointer == start_pointer:
            linkedList[free_list].nextNode = start_pointer
            start_pointer = free_list

        else:
            linkedList[free_list].nextNode = linkedList[previous_pointer].nextNode
            linkedList[previous_pointer].nextNode = free_list
        return True
