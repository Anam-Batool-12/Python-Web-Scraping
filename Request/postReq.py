#program to send a POST request
import requests

r = requests.post("http://httpbin.org/post", data = {'key':'value'})
print(r.text)