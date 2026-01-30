import requests
r = requests.get("https://api.github.com/")
print(r.json())


# import requests # pip install requests

# a = requests.get("https://api.github.com/")
# print(a.json())