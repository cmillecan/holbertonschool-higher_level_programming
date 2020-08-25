#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8).
"""
import urllib.request
from sys import argv


if __name__ == '__main__':
    arg = argv[1]
    try:
        with urllib.request.urlopen(arg) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as error:
        print('Error code:', error.code)
