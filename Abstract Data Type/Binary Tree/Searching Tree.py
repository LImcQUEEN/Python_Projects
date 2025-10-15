ArrayNode = [[0]*3 for x in range(20)]
RootPointer = -1
FreeNode = 0


def searchNode(searchData):
    global ArrayNode
    global RootPointer
    current_pointer = RootPointer
    while current_pointer == -1 and searchData != ArrayNode[current_pointer][1]:
        if searchData > ArrayNode[current_pointer][1]:
            current_pointer = ArrayNode[current_pointer][2]
        else:
            current_pointer = ArrayNode[current_pointer][0]
    return current_pointer