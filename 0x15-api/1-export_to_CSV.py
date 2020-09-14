#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(user_id)).json()
    with open("{}.csv".format(user_id), "w") as f:
        file_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo:
            file_writer.writerow([int(user_id), user.get("username"),
                                  task.get("completed"), task.get("title")])
