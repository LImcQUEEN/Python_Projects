newfile = open("HighScore.txt", "w")
flag = False
while not flag:
    name = input("Please enter guest name: ")
    if name == "No" or name == "no":
        flag = True
    else:
        newfile.write(name + "\n")


newfile.close()
