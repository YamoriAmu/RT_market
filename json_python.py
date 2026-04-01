import json

json_data = '{"name":"Иван","age":30, "is_student": false}'
parset_data = json.loads(json_data)
print(parset_data, type(parset_data))

data = {
    "name":"Мария",
    "age":18,
    "is_student": True
}

json_string = json.dumps(data, indent=4)
print(json_string)

with open("json_example.json", "r", encoding="utf-8") as file:
    read_data=json.load(file)
    print(read_data, type(data))

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data,file, indent=2,ensure_ascii=False)