import json
import csv


with open('users.json', 'r') as f:
    data = json.load(f)

    with open('users.csv', 'w') as csv_f:
        writer = csv.DictWriter(csv_f, ('id', 'name', 'age', 'phone'))
        writer.writeheader()

        phones = (832842, 8382983, 83838389, 838009342, 8234382)
        counter = 0

        for user_id, (name, age) in data.items():
            writer.writerow({'id': user_id, 'name': name, 'age': age, 'phone': phones[counter]})
            counter += 1
