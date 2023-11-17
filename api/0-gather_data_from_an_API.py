#!/usr/bin/python3
""" script that extracts data from an api """
import requests
import sys

def main():
    """ gets the todo list and name of specific employee """
    arg = int(sys.argv[1])
    todo = []
    completed = []
    t_response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    u_response = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for user in u_response:
        if user['id'] == arg:
            name = user['name']
    for item in t_response:
        if item['userId'] == arg:
            todo.append(item)
            if item['completed'] is True:
                completed.append(item['title'])
    print(f'Employee {name} is done with tasks({len(completed)}/{len(todo)})')
    for item in completed:
        print(f'\t {item}')


if __name__ == '__main__':
    main()
