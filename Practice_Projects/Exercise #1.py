taskList = []
print("Welcome to the To-Do List Application")
print("1. Add Task")
print("2. View Task")
print("3. Remove Task")
print("4. Exit")
flag = False
while not flag:
    userChoice = int(input("Please choose an option: "))
    if userChoice == 1:
        newTask = input("Tasks: ")
        taskList.append(newTask)
    elif userChoice == 2:
        for x in range(len(taskList)):
            print(taskList[x])
    elif userChoice == 3:
        removeTask = int(input("Task number to remove: ")) -1
        taskList[removeTask] = " "
    elif userChoice == 4:
        print("GoodBye!")
        flag = True
    else:
        print("Invalid Choice")

