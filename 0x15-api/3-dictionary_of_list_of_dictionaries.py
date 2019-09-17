#!/usr/bin/python3
" export data in the JSON format."
from requests import get
from sys import argv
import json
import requests

if __name__ == "__main__":

    user_l = get('https://jsonplaceholder.typicode.com/users').json()
    dicts = {}
    for user in user_l:
        payload = {'userId': user.get("id")}
        todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params=payload).json()
        complete = []
    for attr in todo:
        complete.append({"task": attr.get("title"),
                          "completed": attr.get("completed"),
                          "username": user.get("username")})
        dicts[user.get("id")] = complete
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(complete, json_file)
