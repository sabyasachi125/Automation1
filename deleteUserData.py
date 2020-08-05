import requests

#API URL
url='https://reqres.in/api/users/2'
#Send GET Request
response=requests.delete(url)
print(response.status_code)
assert response.status_code==204

#Display reponse
print(response.content)
print('******************')
print(response.headers)
