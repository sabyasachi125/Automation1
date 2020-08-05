import requests

#API URL
url='https://reqres.in/api/users?page=2'
#Send GET Request
response=requests.get(url)
print(response.status_code)
assert response.status_code==200

#Display reponse
print(response.content)
print('******************')
print(response.headers)
