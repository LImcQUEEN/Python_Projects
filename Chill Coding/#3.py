# DECLARE Names : ARRAY [0:5] OF STRING
Names = [""] * 6
start_pointer = -1
end_pointer = 0
number_items = 6


def Enqueue(element_p):
    global Names
    global start_pointer
    global end_pointer
    global number_items

    if number_items >= 6:
        return False
    Names[end_pointer] = element_p

    if end_pointer >= 5:
        end_pointer = 0
    else:
        end_pointer = end_pointer + 1
    number_items = number_items + 1
    return True