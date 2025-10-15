arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def insertionsort():
    arraysize = 10
    #in python array start from 0
    for pointer in range(1, arraysize): #outer loop start from 1 because we take the element at first index as aur reference element
        valuetoinsert = arrayData[pointer]
        holeposition = pointer #we don't want any affect our pointer value
        #holeposition is the varialbe that start from pointer and from it's
        #starting position it goes back until it reach it's correct position

        while (holeposition>0) and (arrayData[holeposition-1]<valuetoinsert):
            #for decending sign will be <
            #for assending sign will be >
            arrayData[holeposition] = arrayData[holeposition-1]
            holeposition = holeposition - 1

        arrayData[holeposition] = valuetoinsert
insertionsort()
print(arrayData)
