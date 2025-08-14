import os

completed_tasks = []

def countTasks():
    with open(r"tasks.txt", 'r') as fr:
        numTasks = len(fr.readlines())
        return int(numTasks)

def viewTask():
    print("To Do: \n")
    
    try:
        with open(r"tasks.txt", 'r') as fr:
            for line in fr:
                print(line, end='')
    except:
        print("\nERROR in viewing Tasks")

def addTask():
    numTasks = countTasks() + 1

    try:
        with open(r'tasks.txt', 'a') as fw:
            new_task = input("\nNew Task: ")
            task = "[" + str(numTasks) + "]: " + new_task + "\n"
            print(task)

            fw.write(task)

            print("\nTask Added!")
    except:
        print("\nERROR in adding Tasks")

def completedTask():
    try:
        with open('tasks.txt', 'r') as fr:
            print(fr.read())
            lines = fr.readlines()
       
        if not lines:
            print("File is empty!")
            return

        num = int(input("Wich task do you want to mark as completed"))
        
        if num < 1 or num > len(lines):
            print("Invalid line number!!")
            return

        with open('tasks.txt', 'w') as fw:
            for i,line in enumerate(lines, 1):
                if i != num:
                    fw.write(line)
                
        print("Task marked as completed!!")

    except ValueError:
        print("Please enter a valid number!!")
    except:
        print("Oops!! Something went wrong!")


def deleteTask():
    try:
        with open('tasks.txt', 'r') as fr:
            print(fr.read())

            lines = fr.readlines()

        ptr = 1

        number = int(input("Wich task do you want to delete??"))

        with open('tasks.txt', 'w') as fw:
            for line in lines:
                if ptr != number:
                    fw.write(line)
                ptr += 1

        print("Task deleted!!")

    except:
        print("Oops !! Something went wrong!")
    

if __name__ == "__main__":
    os.system('clear')
    while True:
        print("\nPlease select one of the following options: ")
        print("--------------------------------------------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Completed Task")
        print("4. Delete Task")
        print("5. Exit")

        opt = input("Option:\t")

        if(opt == '1'):
           os.system('clear')
           viewTask()
        elif(opt == '2'):
           os.system('clear')
           addTask()
        elif(opt == '3'):
           os.system('clear')
           completedTask()
        elif(opt == '4'):
            os.system('clear')
            deleteTask()
        elif(opt == '5'):
            exit()
        else:
            os.system('clear')
            print("Invalid input try again!!!")
            
    
