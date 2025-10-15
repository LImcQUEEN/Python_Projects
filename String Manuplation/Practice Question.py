name = input("Naam Bata!! ")
first_len = 0
for x in range(len(name)):
    if name[x] != " ":
        first_len = first_len + 1
    else:
        break
first_name = name[0:first_len]
last_name = name[first_len+1 : len(name)]
print(first_name)
print(last_name)