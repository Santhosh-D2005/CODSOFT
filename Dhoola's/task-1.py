tasks = []
def add_task():
    task = input("Enter a new task:")
    tasks.append(task)
    print(f"Task '{task}' added successfullly!")

def view_tasks():
    if not tasks:
        print("No tasks int the list")
        return
    
    print ("Your task:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

def remove_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n----SIMPLE TO-DO LIST----")
        print("1. ADD TASK")
        print("2. VIEW TASKS")
        print("3. REMOVE TASK")
        print("4.EXIT!!!")

        choice = input("Enter your choice (1-4):")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Meet you later")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()                   
