import requests
import json

url = 'https://reqres.in/api/users'
file = open('C:\\Users\\Arman\\PycharmProjects\\requests\\file\\createUser.json')
json_input = file.read()
json_request = json.loads(json_input)
json_response = requests.post(url, json_request)
print(json_response, ' - ', json_response.content)
