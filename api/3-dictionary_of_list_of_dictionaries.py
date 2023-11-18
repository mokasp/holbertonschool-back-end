#!/usr/bin/python3
""" script that extracts data from an api and inserts it into a JSON file """
import json
import requests
import sys


def main():
    """ gets the todo list items of all user and saves it to a
    JSON file """
    user_dict = {}
    url = 'https://jsonplaceholder.typicode.com'
    user_r = requests.get(f'{url}/users').json()
    for i in range(len(user_r)):
        temp_list = []
        the_user = user_r[i]
        user_id = the_user['id']
        username = the_user['username']
        todo_r = requests.get(f'{url}/users/{user_id}/todos').json()
        for item in todo_r:
            tmp = {}
            tmp.update({"task": item['title'], "completed": item['completed']})
            tmp.update({"username": username})
            temp_list.append(tmp)
            user_dict.update({user_id: temp_list})
    with open('todo_all_employees.json', "w") as f:
        json.dump(user_dict, f)


if __name__ == '__main__':
    main()
