import json


users = {
    123456: ('Victor', 24),
    123457: ('Dima', 30),
    123458: ('Alex', 16),
    123459: ('Hilary', 18),
    123450: ('John', 21),
}

with open('users.json', 'w') as f:
    json.dump(users, f, indent=4)
