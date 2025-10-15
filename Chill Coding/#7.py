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


def ordered_insertion():
    global start_pointer
    global empty_list
    global linkedList
    data_to_insert = int(input("Enter Data to Add: "))
    if empty_list < 0 or empty_list > 9:
        return False
    else:
        free_list = empty_list
        empty_list = linkedList[empty_list].Pointer
        new_node = Node(data_to_insert, -1)
        linkedList[free_list] = new_node
        current_pointer = start_pointer
        previous_pointer = 0
        while current_pointer != -1 and data_to_insert > linkedList[current_pointer].Pointer:
            previous_pointer = current_pointer
            current_pointer = linkedList[current_pointer].Pointer
        if start_pointer == current_pointer:
            linkedList[free_list].Pointer = start_pointer
            start_pointer = free_list
        else:
            linkedList[free_list].Pointer = linkedList[previous_pointer].Pointer
            linkedList[previous_pointer].Pointer = free_list
        return True
