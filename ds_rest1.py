import json
input ='''[
    {"ID":"001", "x":"2", "name":"Chuck"},
    {"ID":"002", "x":"3", "name":"Break"}
]'''
input
type(input)
info=json.loads(input)
type(info)
info0=info[0]
info0['ID']
for item in info:
    print item['ID'], item['name']