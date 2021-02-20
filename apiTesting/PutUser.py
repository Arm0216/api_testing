import requests
import json

url = 'https://reqres.in/api/users/2'

file = open('C:\\Users\\Arman\\PycharmProjects\\requests\\file\\createUser.json')
json_input = file.read()
json_request = json.loads(json_input)
response = requests.put(url, json_request)
print(response, ' - ', response.content)


