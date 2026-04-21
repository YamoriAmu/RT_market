import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.status_code)
print(response.json())




data = {
    "title":"Новая задача",
    "completed": False,
    "userID": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos",json=data)
print(response.status_code)
print(response.request.headers)
print(response.json())



data = {"username":"test_user","pass": "123456" }
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.json())


headers = {"Autorization":"Barer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.request.headers)
print(response.json())


response = httpx.get('https://jsonplaceholder.typicode.com/todos?userId=1')
print(response.url)
print(response.json())


files = {"file":("example.txt",open("example.txt","rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())

with httpx.Client() as client:
   response1 = client.get("https://jsonplaceholder.typicode.com/todos?userId=1")
   response2 = client.get("https://jsonplaceholder.typicode.com/todos?userId=2")
print(response1.json())
print(response2.json())

client = httpx.Client(headers={"Autorization":"Barer my_secret_token"})
response = client.get("https://httpbin.org/get")

print(response.json())