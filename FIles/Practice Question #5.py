new_file = open("EventGuest.txt", "r")
flag = False
for line in new_file:
    if line.strip() == "Papersdock":
        print("It's Already There! ")
        flag = True
new_file.close()
new_file = open("EventGuest.txt", "a")
if not flag:
    new_file.write("Papersdock\n")