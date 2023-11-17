#!/usr/bin/python3
""" script that extracts data from an api and inserts it into a JSON file """
import json
import requests
import sys


def main(user_id):
    """ gets the todo list items of a specific user and saves it to a
    JSON file """
    user_dict = {}
    temp_list = []
    url = 'https://jsonplaceholder.typicode.com'
    todo_r = requests.get(f'{url}/users/{user_id}/todos').json()
    user_r = requests.get(f'{url}/users/{user_id}').json()
    for item in todo_r:
        temp = {}
        temp.update({"task": item['title'], "completed": item['completed']})
        temp.update({"username": user_r['username']})
        temp_list.append(temp)
        user_dict.update({str(user_id): temp_list})
    print(len(temp_list))
    with open(f'{user_id}.json', "w") as f:
        json.dump(user_dict, f)


if __name__ == '__main__':
    main(int(sys.argv[1]))
