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


def insertion(elementP):
    global linkedList
    global start_pointer
    global empty_pointer
    if empty_pointer < 0 or empty_pointer > 9:
        print("LinkedList if full")
    else:
        freeList = empty_pointer
        empty_pointer = linkedList[elementP].nextNode
        newNode = Node(elementP, -1)
        linkedList[freeList] = newNode
        previousPointer = 0
        currentPointer = start_pointer
        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
        linkedList[previousPointer].nextNode = freeList


def deletion(elementP):
    global linkedList
    global start_pointer
    global empty_pointer
    previousPointer = 0
    currentPointer = start_pointer
    freeList = empty_pointer
    empty_pointer = linkedList[empty_pointer].nextNode
    while currentPointer != -1 and linkedList[currentPointer].data < elementP:
        previousPointer = currentPointer
        currentPointer = linkedList[currentPointer].nextNode
    if currentPointer == -1:
        print("Value Not Found")
    else:
        if start_pointer == currentPointer:
            start_pointer = linkedList[currentPointer].nextNode
        else:
            linkedList[previousPointer].nextNode = linkedList[currentPointer].nextNode

        linkedList[currentPointer].data = 0
        linkedList[currentPointer].nextNode = freeList
        freeList = currentPointer
