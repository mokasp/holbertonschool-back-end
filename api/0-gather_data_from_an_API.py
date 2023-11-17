#!/usr/bin/python3
import requests
import sys
arg = int(sys.argv[1])
todo = []
completed = []
todo_response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
user_response = requests.get('https://jsonplaceholder.typicode.com/users').json()
for user in user_response:
    if user['id'] == arg:
        employee_name = user['name']
for item in todo_response:
    if item['userId'] == arg:
        todo.append(item)
        if item['completed'] == True:
            completed.append(item['title'])
print(f'Employee {employee_name} is done with tasks({len(completed)}/{len(todo)})')
for item in completed:
    print(f'\t {item}')
