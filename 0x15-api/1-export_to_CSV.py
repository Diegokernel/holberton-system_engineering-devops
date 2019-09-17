#!/usr/bin/python3
"export data in the CSV format."
from requests import get
from sys import argv
import csv

if __name__ == "__main__":

    user = get('https://jsonplaceholder.typicode.com/users/{}'
               .format(argv[1])).json()
    todo = get('https://jsonplaceholder.typicode.com/todos?userId={}'
               .format(argv[1])).json()

    with open('{}.csv'.format(argv[1]), 'w') as employee_file:
        employee_writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL)
        for attr in todo:
            employee_writer.writerow([attr.get('userId'), user.get('username'),
                                      attr.get('completed'),
                                      attr.get('title')])
