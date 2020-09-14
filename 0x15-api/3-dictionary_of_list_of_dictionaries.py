#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.
"""
import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_task_d = {}
    username_d = {}
    for user in users:
        user_id = user.get("id")
        user_task_d[user_id] = []
        username_d[user_id] = user.get("username")
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for task in todo:
        values_dict = {}
        user_id = task.get("userId")
        values_dict["task"] = task.get("title")
        values_dict["completed"] = task.get("completed")
        values_dict["username"] = username_d.get(user_id)
        user_task_d.get(user_id).append(values_dict)
    with open("todo_all_employees.json", "w") as f:
        json.dump(user_task_d, f)
