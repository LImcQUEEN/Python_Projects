file = open("HighScore", "r")
for lines in file:
    text = file.readline()
    print(text)
file.close()
