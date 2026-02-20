#working with the json module
import json
#using json.loads
json_str = '{"id": true,"name": "Alice"}'
py_obj = json.loads(json_str)
print(type(py_obj),py_obj)

# using json.dumps
p_obj = {"id": True,
  "name": "Alice"}
j_str = json.dumps(p_obj)
print(type(j_str),j_str)