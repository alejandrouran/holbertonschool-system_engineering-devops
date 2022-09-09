#!/usr/bin/python3
"""
 to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    username = user.get('username')
    tasks = []
    for task in todos:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[sys.argv[1]] = tasks
    with open("{}.json".format(sys.argv[1]), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
