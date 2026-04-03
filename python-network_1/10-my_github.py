#!/usr/bin/python3
"""
This module takes your GitHub credentials and uses the GitHub API
to display your id.
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    try:
        print(response.json().get('id'))
    except ValueError:
        print("None")
