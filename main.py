
import os
import pickle  # It will act as a database
from datetime import datetime

# Intialize an empty list to store the tasks
todos = []
# Define the file name to store the tasks
TODO_FILE = "todos.pkl"


# define a class to represent each todo item
class Todo:
    def __init__(self, title, created_at, is_completed=False):
        self.title = title
        self.created_at = created_at
        self.is_completed = is_completed


# Function to save todos to our pickle file
def save_todos():
    with open(TODO_FILE, "wb") as file:
        pickle.dump(todos, file)

# Function to read todos from the pickle file
def read_from_file():
    global todos
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "rb") as file:
            todos = pickle.load(file)


# Function to add a new todo item
def add_todo():
    title = input("Enter the task: ")
    created_at = datetime.now().strftime("%d/%m %H:%M")
    todo = Todo(title, created_at)
    todos.append(todo)
    save_todos()
    print("Task added successfully!")


# Function to list all the todo items
def list_todos():
    print("+----+-------------------------------------+--------------+--------------+")
    print("| ID |             Todo Title              |  Created At  |  Completed   |")
    print("+----+-------------------------------------+--------------+--------------+")

    # Iterate through all the todos and print each item
    for i, todo in enumerate(todos):
        print(f"| {i+1:2} | {todo.title:35} | {todo.created_at:^12} | { "✅" if todo.is_completed else "❌":^11} |")
    print("+----+-------------------------------------+--------------+--------------+")

def mark_as_complete():
    try:
        list_todos()
        todo_id = int(input("Enter the ID of the task : "))-1
        todos[todo_id].is_completed = True
        save_todos()
        print("Task marked as complete successfully!")
    except IndexError:
        print("Invalid task ID. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_todo():
    try:
        list_todos()
        todo_id = int(input("Enter the ID of the task : "))-1
        del todos[todo_id]
        save_todos()
        print("Task deleted successfully!")
    except IndexError:
        print("Invalid task ID. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_menu():
    while True:
        print("Welcome, KayKei ! ")
        choice = input("Type 'A' to add, 'D' to delete, 'W' to mark as complete, 'S' to quit\n").upper()
        if choice == 'A':
            add_todo()
        elif choice == 'D':
            delete_todo()
        elif choice == 'W':
            mark_as_complete()
        elif choice == 'S':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        list_todos()

# To check if the file exists
def is_this_first_time():
    if os.path.exists(TODO_FILE):
        read_from_file()
        list_todos()
    else:
        print("Welcome, KayKei ! ")
        add_todo()
        list_todos()


if __name__ == "__main__":
    # clearing the console
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;32;92m To-Do List ! \033[0;37;92m")
    is_this_first_time()
    show_menu()
