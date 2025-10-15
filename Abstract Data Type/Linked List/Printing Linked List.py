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


def outputNodes():
    global linkedList
    global start_pointer
    current_pointer = start_pointer
    while current_pointer != -1:
        print(linkedList[current_pointer].data)
        current_pointer = linkedList[current_pointer].nextNode


outputNodes()