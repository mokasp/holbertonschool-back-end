#!/usr/bin/python3
""" script that extracts data from an api """
import requests
import sys


def main(user_id):
    """ gets the todo list and name of specific employee """
    url = 'https://jsonplaceholder.typicode.com'
    todo = []
    completed = []
    todo_r = requests.get(f'{url}/todos').json()
    user_r = requests.get(f'{url}/users/{user_id}').json()
    name = user_r.get('name')
    for item in todo_r:
        if item['userId'] == user_id:
            todo.append(item)
            if item['completed'] is True:
                completed.append(item['title'])
    done = len(completed)
    all_ = len(todo)
    print(f'Employee {name} is done with tasks({done}/{all_}):')
    for item in completed:
        print(f'\t {item}')


if __name__ == '__main__':
    main(int(sys.argv[1]))
