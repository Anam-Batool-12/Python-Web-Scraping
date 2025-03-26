#simple example of how to use the requests library to make a GET request to the Google homepage.
import requests
r = requests.get("https://www.google.com")
print(r.text)
with open("google.html", "w") as f:
    f.write(r.text)