tasks = []


def add_task(task):
    """Add a new task to the list."""
    tasks.append(task)
    print(f"Task added: {task}")


def remove_task(task):
    """Remove a task from the list if it exists."""
    if task in tasks:
        tasks.remove(task)
        print(f"Task removed: {task}")
    else:
        print(f"Task '{task}' not found in the list.")


def display_tasks():
    """Display all tasks in the list."""
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("The to-do list is empty.")


def main():
    """Main loop to interactively add, remove, and display tasks."""
    print("Welcome to the To-Do List Manager!")
    print("Commands: 'add [task]', 'remove [task]', 'show', 'exit'")

    while True:
        command = input("Enter a command: ").strip()

        if command.lower() == "exit":
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        elif command.lower() == "show":
            display_tasks()
        elif command.startswith("add "):
            task = command[4:].strip()
            if task:
                add_task(task)
            else:
                print("Please specify a task to add.")
        elif command.startswith("remove "):
            task = command[7:].strip()
            if task:
                remove_task(task)
            else:
                print("Please specify a task to remove.")
        else:
            print(
                "Invalid command. Use 'add [task]', 'remove [task]', 'show', or 'exit'.")


if __name__ == "__main__":
    main()
    # add_task("Buy groceries")
    # add_task("Read a book")
    # display_tasks()
    # remove_task("Read a book")
    # display_tasks()
