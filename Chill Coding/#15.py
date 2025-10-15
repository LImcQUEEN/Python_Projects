name = input("Enter your name: ")
startIndex = 0
totalIndex = len(name)
for x in range(0, totalIndex):
    if name[x] != " ":
        startIndex = startIndex + 1
    else:
        break
firstname = name[0:startIndex]
lastname = name[startIndex+1:totalIndex]
print(firstname)
print(lastname)