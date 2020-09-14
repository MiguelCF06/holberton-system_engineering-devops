#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(user_id)).json()
    username = user.get("username")
    all_tasks = []
    for task in todo:
        values_dict = {}
        values_dict["task"] = task.get("title")
        values_dict["completed"] = task.get("completed")
        values_dict["username"] = username
        all_tasks.append(values_dict)
    obj = {}
    obj[user_id] = all_tasks
    with open("{}.json".format(user_id), "w") as f:
        json.dump(obj, f)
