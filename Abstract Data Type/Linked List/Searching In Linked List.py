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


def searchList():
    global linkedList
    global start_pointer
    valueSearch = input("Enter Value to Search :")
    current_pointer = start_pointer
    previous_pointer = 0
    while current_pointer != -1:
        if linkedList[current_pointer] != valueSearch:
            current_pointer = linkedList[current_pointer].nextNode
        else:
            return current_pointer
    current_pointer = -1
    return current_pointer