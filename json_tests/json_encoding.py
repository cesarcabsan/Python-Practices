import json

# Encoding
records = [
    {'id': 1, 'amount': 1500.75},
    {'id': 2, 'amount': 20000.00}
]
encode = json.JSONEncoder().encode(records)
print(encode)

# Decoding
raw_json = '{"product": "Laptop", "price": 999.99, "in_stock": true}'
decode = json.JSONDecoder().decode(raw_json)
print(decode, type(decode))

# combining both
data = ['Ralesh', {'marks': (50, 60, 70)}]
e = json.JSONEncoder()
s = e.encode(data)
print("Encoded:", s)
d = json.JSONDecoder()
obj = d.decode(s)
print("Decoded:", obj, type(obj))

