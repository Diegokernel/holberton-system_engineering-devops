#!/usr/bin/python3
" export data in the JSON format."
from sys import argv
import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    the_dict = {}
    for user in users:
        complete = []
        user_id = user.get('id')
        username = user.get('username')
        for attr in todo:
            if user_id == attr.get('userId'):
                info = {
                    'task': attr.get('title'),
                    'completed': attr.get('completed'),
                    'username': username,
                }
                complete.append(info)
            dictu = {user_id: complete}
        the_dict.update(dictu)
    with open('todo_all_employees.json', 'w') as f:
        json.dump(the_dict, f)
