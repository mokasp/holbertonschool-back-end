#!/usr/bin/python3
""" script that extracts data from an api and inserts it into a CSV file """
import csv
import requests
import sys


def main(user_id):
    """ gets the todo list items of a specific user and saves it to a
    CSV file """
    lists = []
    url = 'https://jsonplaceholder.typicode.com'
    todo_r = requests.get(f'{url}/users/{user_id}/todos').json()
    user_r = requests.get(f'{url}/users/{user_id}').json()
    for item in todo_r:
        csv_list = [user_id, user_r['username']]
        csv_list.append(item['completed'])
        csv_list.append(item['title'])
        lists.append(csv_list)
    with open(f'{user_id}.csv', 'w') as f:
        the_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for item in lists:
            the_writer.writerow(item)


if __name__ == '__main__':
    main(int(sys.argv[1]))
