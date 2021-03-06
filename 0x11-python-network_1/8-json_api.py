#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == '__main__':
    data = {'q': ''}
    if len(argv) > 1:
        data['q'] = argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        data = req.json()
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
