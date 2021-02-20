import requests
import json
import jsonpath

url = 'https://reqres.in/api/users?page=2'

#positive
response = requests.get(url)
print(response, ' - ', response.content)
print(response.headers)

#With json
response_json = json.loads(response.text)
print(response_json)
page = jsonpath.jsonpath(response_json, 'page')
print(page[0])

#negative
url = 'https://reqres.in/api/users/15'
response = requests.get(url)
print(response)
# file = open('C:\\Users\\Arman\\Desktop\\api\\createUser.json', 'r')
# json_input = file.read()
# request_json = json.loads(json_input)
# response = requests.post(url, request_json)
# print(response)
# response_json = json.loads(response.text)
# id = jsonpath.jsonpath(response_json, 'name')
# print(id)
#
# json_response = json.loads(response.text)
# print(json_response)
#
# pages = jsonpath.jsonpath(json_response, '')

# print(response.content)