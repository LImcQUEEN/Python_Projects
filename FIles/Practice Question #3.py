file = open("HighScore.txt", "r")
FileData = [[""]*2 for x in range(10)]
for row in range(10):
    FileData[row][0] = file.readline().strip()
    FileData[row][1] = file.readline().strip()

print(FileData)
file.close()


def OutputHighScore():
    for x in range(10):
        combine = FileData[x][0] + "  " + FileData[x][1]
        print(combine)





