import json

people_string = '''
{
    "people": [
    {
    "name": "S Martin",
    "phone": "543-666-4123",
    "emails": ["s.martin@bugsmail.com", "martin.s@workmail.com"],
    "has_license": false
    },
    {
    "name": "Joe Lein",
    "phone": "543-666-7281",
    "emails": ["joe.lein@bugsmail.com", "lein.joe@workmail.com"],
    "has_license": true
    }
 ]
}
'''
data = json.loads(people_string)

print(data)

# print(type(data))
# print(type(data['people']))

for person in data['people']:
    print(person['name'])

for person in data['people']:
    del person['phone']

new_str = json.dumps(data, indent=2, sort_keys=True)

print(new_str)