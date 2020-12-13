import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    # Using reader()
    #csv_data = csv.reader(data_file)
    

    # We don't want headers or first line of bad data
    # next(csv_data)
    # next(csv_data)

    # for line in csv_data:
    #     #print(line)

    #     if line[0] == 'No Reward':
    #         break
    #     names.append(f'{line[0]} {line[1]}')

    # Using DictReader()
    csv_data = csv.DictReader(data_file)

    # We don't want first line of bad data
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p> There are currently {len(names)} public contributors. Thank You!! </p>'
#print(html_output)

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
print(html_output)

# for name in names:
#     print(name)
    