ArrayNode = [[0]*3 for x in range(20)]
RootPointer = -1
FreeNode = 0


def AddNode():
    global ArrayNode
    global RootPointer
    global FreeNode
    newNode = int(input("Enter Data to Add: "))
    if FreeNode <= 19:
        ArrayNode[FreeNode][0] = -1
        ArrayNode[FreeNode][1] = newNode
        ArrayNode[FreeNode][2] = -1

        if RootPointer == -1:
            RootPointer = 0
        else:
            found = False
            CurrentPointer = RootPointer
            while not found:
                if newNode < ArrayNode[CurrentPointer][1]:
                    if ArrayNode[CurrentPointer][0] == -1:
                        ArrayNode[CurrentPointer][0] = FreeNode
                        found = True
                    else:
                        CurrentPointer = ArrayNode[CurrentPointer][0]
                else:
                    if ArrayNode[CurrentPointer][2] == -1:
                        ArrayNode[CurrentPointer][2] = FreeNode
                        found = True
                    else:
                        CurrentPointer = ArrayNode[CurrentPointer][2]

        FreeNode = FreeNode + 1
    else:
        print("Tree is Full")


AddNode()
AddNode()
AddNode()
AddNode()
AddNode()
AddNode()
AddNode()


for x in range(20):
    print(ArrayNode[x])
