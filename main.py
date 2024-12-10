import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect("todo.db")  # Creates or connects to a database file
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
    )
    """)
    conn.commit()
    return conn

# Display menu
def display_menu():
    print("\n=== To-Do List App ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# View tasks
def view_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, task FROM tasks")
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for task in tasks:
            print(f"{task[0]}. {task[1]}")

# Add task
def add_task(conn):
    task = input("Enter the task: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    print(f"'{task}' has been added to your list.")

# Remove task
def remove_task(conn):
    view_tasks(conn)
    try:
        task_id = int(input("Enter the ID of the task to remove: "))
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Task {task_id} has been removed.")
        else:
            print("Task not found.")
    except ValueError:
        print("Please enter a valid task ID.")

# Main function
def main():
    conn = init_db()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(conn)
        elif choice == "2":
            add_task(conn)
        elif choice == "3":
            remove_task(conn)
        elif choice == "4":
            print("Exiting To-Do List App. Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
