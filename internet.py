import requests


# response = requests.get('https://google.com')
# print(f"{response.status_code=}")  # 200
#
#
# method = "GET"
# response = requests.request(url='https://google.com', method=method)
# print(f"{response.status_code=}")
# print(f"{response.content=}")  # content of the HTML page or body of API response


url = "https://jsonplaceholder.typicode.com/comments"
my_params = {"postId": 1}

# option 1
response = requests.get(url, params=my_params)
print(f"{response.status_code=}")
# print(f"{response.content=}")
print(f"{response.json()=}")

# option 2
response = requests.request(url=url, method="GET", params=my_params)
print(f"{response.status_code=}")

# option 3
response = requests.get(url=f'{url}?postId=1')
print(f"{response.status_code=}")
