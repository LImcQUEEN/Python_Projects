Marks = [10, 20, 25, 33, 47, 56, 63]


def BinarySearch(search_number):
    upper_bound = 5
    lower_bound = 1
    value_found = False
    not_in_list = False
    while not value_found and not not_in_list:
        mid_point = int((upper_bound+lower_bound)/2)
        if search_number == Marks[mid_point]:
            value_found = True
            return value_found
        else:
            if search_number > Marks[mid_point]:
                lower_bound = mid_point + 1
            elif search_number < Marks[mid_point]:
                upper_bound = mid_point - 1
        if lower_bound > upper_bound:
            not_in_list = True


temp = BinarySearch(2)
if temp:
    print("Value Found")
else:
    print("Value Not Found")