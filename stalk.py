#!/bin/python
import requests

username = input("Insert username to stalk: ")

# Check on github
res = requests.get('http://github.com/'+username)
if res.status_code==404:
    print("User not found on github")
else:
    print(username, 'found on github')

res = requests.get('http://instagram.com/'+username)
if res.status_code==404:
    print("User not found on instagram")
else:
    print(username, 'found on instagram')

res = requests.get('http://codeforces.com/profile/'+username)
busername = bytes(username, 'ascii')
if busername not in res.content:
    print("User not found on codeforces")
else:
    print(username, 'found on codeforces')