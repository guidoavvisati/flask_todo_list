import random


def query_name():
    return random.choice(["Alice", "Bob", "Chris", "Dolly"])


def fetch_todo():
    todo_list = [
        {"id": 1, "task": "Task 1", "status": "In Progress"},
        {"id": 2, "task": "Task 2", "status": "Todo"},
    ]
    return todo_list
