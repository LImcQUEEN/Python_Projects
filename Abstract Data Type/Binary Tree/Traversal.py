FreeNode = 0
RootPointer = 0
BinaryTree = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]


def Inorder(Root):  # LEFT ROOT RIGHT
    global BinaryTree
    if BinaryTree[Root][0] != -1:   # This means if left value not -1 move to that value
        Inorder(BinaryTree[Root][0])    # In this line we traverse toward left
    print(BinaryTree[Root][1])  # We print the root value
    if BinaryTree[Root][2] != -1:   # Here we are checking right value if not -1 move to that value
        Inorder(BinaryTree[Root][2])    # In this line we travers toward right


def Preorder(Root):  # ROOT LEFT RIGHT
    global BinaryTree
    print(BinaryTree[Root][1])  # First we will print root value
    if BinaryTree[Root][0] != -1:   # Checks if left value is -1
        Inorder(BinaryTree[Root][0])    # If not traverse to that value
    if BinaryTree[Root][2] != -1:   # Check if right value is -1
        Inorder(BinaryTree[Root][2])    # If not travers to that value


def PostOrder(Root):  # LEFT RIGHT ROOT
    global BinaryTree
    if BinaryTree[Root][0] != -1:   # Check if left value is -1
        Inorder(BinaryTree[Root][0])    # if not traverse to that value
    if BinaryTree[Root][2] != -1:   # check if right value is -1
        Inorder(BinaryTree[Root][2])    # if not travers to that value
    print(BinaryTree[Root][1])  # at the end print root value


temp = input("Which Traversal you would like to do: ")
if temp.lower() == "in":
    Inorder(0)
elif temp.lower() == "pre":
    Preorder(0)
elif temp.lower() == "post":
    PostOrder(0)
else:
    print("Invalid Traversal")