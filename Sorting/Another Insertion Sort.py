Marks = [10, 23, 17, 15, 7, 21, 19, 20, 5, 2]
for pointer in range(1, 10):
    valueInsert = Marks[pointer]
    holePosition = pointer
    while holePosition > 0 and Marks[holePosition-1] > valueInsert:
        Marks[holePosition] = Marks[holePosition-1]
        holePosition = holePosition - 1
    Marks[holePosition] = valueInsert

print(Marks)