#!/usr/bin/python3
"""
to export data in the JSON format.
"""

import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users').json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user_dict.get("id"): [{
                "task": task_dict.get("title"),
                "completed": task_dict.get("completed"),
                "username": user_dict.get("username")
            } for task_dict in requests.get(url + "todos",
                                    params={"userId": user_dict.get("id")}).json()]
            for user_dict in user}, jsonfile)