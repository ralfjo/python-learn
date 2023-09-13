import json

with open("sample.json", mode="r") as f:
    data = json.loads(f.read())
    print(data['type'])
    