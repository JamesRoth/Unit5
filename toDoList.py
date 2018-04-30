#James Roth
#4/30/18
#toDoList.py - makes a list of things to do

tasks = []

while True:
    task=input("Enter a command (add, delete, print, quit): ")
    if task == "quit":
        break
    elif task[0] == "a":
        tasks.append(task[3:])
    elif task[0] == "d":
        tasks.remove(task[6:])
    else:
        for item in tasks:
            print(item)
