#simple example of how to use the requests library to make a GET request to the GitHub API.
import requests
r = requests.get('https://api.github.com/events')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
