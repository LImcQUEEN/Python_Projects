file = open("HighScore.txt", "r")
Sum = 0
for lines in file:
    text = file.readline()
    score = file.readline()
    Sum = Sum + int(score)
file.close()
print(Sum)
