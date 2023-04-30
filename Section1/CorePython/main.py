import json

items = json.loads('[{"id": 1, "text": "Item 1"}, {"id": 2, "text": "Item 2"}]')

for item in items:
    print(item["text"])

print("Hello")
print("Hello")
