import requests

r = requests.get("http://python.org")
print(r.status_code)

print(r.content)
print(b'Python is a programming language' in r.content)