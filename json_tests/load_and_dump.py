import json

# JSON object to python (json.loads)
json_test = '{"id": 1001, "name": "Arnold", "age": 26, "city": "New York"}'
convert_to_python = json.loads(json_test)
print(convert_to_python["city"])

# Python object to JSON (json.dumps)
py_object = {"id": 1001, "name": "Arnold", "age": 26, "city": "New York"}
convert_to_json = json.dumps(py_object)
print(convert_to_json)
