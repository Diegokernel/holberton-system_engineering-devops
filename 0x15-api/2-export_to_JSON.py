#!/usr/bin/python3
" export data in the JSON format."
from requests import get
from sys import argv
import json

if __name__ == "__main__":

    user = get('https://jsonplaceholder.typicode.com/users/{}'
               .format(argv[1])).json()
    todo = get('https://jsonplaceholder.typicode.com/todos?userId={}'
               .format(argv[1])).json()

    complete = []
    for attr in todo:
        complete.append({"task": attr.get("title"),
                          "completed": attr.get("completed"),
                          "username": user.get("username")})
    with open('{}.json'.format(argv[1]), 'w') as json_file:
        json.dump({argv[1]: complete}, json_file)
