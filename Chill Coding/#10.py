ArrayNode = [[0]*3 for x in range(20)]
RootPointer = -1
FreeNode = 0


def addNode():
    global ArrayNode
    global RootPointer
    global FreeNode
    dataAdd = int(input("Enter Data to Add: "))
    if FreeNode <= 19:
        ArrayNode[FreeNode][0] = -1
        ArrayNode[FreeNode][1] = dataAdd
        ArrayNode[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            CurrentPointer = RootPointer
            found = False
            while not found:
                if dataAdd > ArrayNode[CurrentPointer][1]:
                    if ArrayNode[CurrentPointer][2] == -1:
                        ArrayNode[CurrentPointer][2] = FreeNode
                    else:
                        CurrentPointer = ArrayNode[CurrentPointer][2]
                else:
                    if ArrayNode[CurrentPointer][0] == -1:
                        ArrayNode[CurrentPointer][0] = FreeNode
                    else:
                        CurrentPointer = ArrayNode[CurrentPointer][0]
        FreeNode = FreeNode + 1
    else:
        print("Tree is Full")


def searchTree(data_s):
    global ArrayNode
    global RootPointer
    CurrentPointer = RootPointer
    while CurrentPointer != -1 and ArrayNode[CurrentPointer][1] != data_s:
        if data_s > ArrayNode[CurrentPointer][1]:
            CurrentPointer = ArrayNode[CurrentPointer][2]
        else:
            CurrentPointer = ArrayNode[CurrentPointer][0]
    return CurrentPointer