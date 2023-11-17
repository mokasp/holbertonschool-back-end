#!/usr/bin/python3
""" script that extracts data from an api and inserts it into a JSON file """
import requests
import sys


def main(user_id):
    """ gets the todo list items of a specific user and saves it to a
    JSON file """
    lists = []
    url = 'https://jsonplaceholder.typicode.com'
    todo_r = requests.get(f'{url}/users/{user_id}/todos').json()
    user_r = requests.get(f'{url}/users/{user_id}').json()



if __name__ == '__main__':
    main(int(sys.argv[1]))
