#to_do_list.py
# todo.py

# ---------- To-Do List Application ----------

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Add a new task
def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f" Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n---- Your To-Do List ----")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("-------------------------\n")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter the task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f" Task '{removed}' removed.")
            else:
                print(" Invalid task number.")
        except ValueError:
            print(" Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\n==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        print("=========================")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please select between 1-4.")

if __name__ == "__main__":
    main()
