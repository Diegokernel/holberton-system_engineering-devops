#!/usr/bin/python3
" returns information about his/her TODO list progress."
from requests import get
from sys import argv

if __name__ == "__main__":
    complete = []
    user = get('https://jsonplaceholder.typicode.com/users/{}'
               .format(argv[1])).json()
    todo = get('https://jsonplaceholder.typicode.com/todos?userId={}'
               .format(argv[1])).json()
    for attr in todo:
        if attr.get('completed') is True:
            complete.append(attr.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(user.get('name'), len(complete), len(todo)))
    for title in complete:
        print('\t {}'.format(title))
