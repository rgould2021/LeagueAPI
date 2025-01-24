'''Given a string, sort it in decreasing order based on the frequency of characters. 
If there are multiple possible solutions, return any of them.
For example, given the string tweet, return tteew. eettw would also be acceptable.'''
tasks = []
i=0
def addTask(task):
    tasks.append(task)
    print("Task addded!")
def delTask(tasks):
    del tasks[task]
    i = input("Enter a task number to be deleted.")
def viewtask(tasks):
    for i,task in enumerate(tasks):
        print(f"{i+1} + {tasks}")
while True:
    print("Enter a number \n1. Add Task to list \n2. View Task \n3. Delete Task \n4. Exit program\n")
    choice = input("Enter your choice: ")
    if x == 1:
        input("Enter the task")
        addTask(tasks)
    elif x==2:
        viewtask(tasks)
    elif x==3:
        delTask
    elif x==4:
        exit