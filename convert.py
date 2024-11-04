from pprint import pprint
import csv

key_dict = {}

with open('keys.csv', mode = 'r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
      if line[0] == '':
          continue
      key_dict[line[0]] = {
            'col': line[1],
            'row': line[2],
            'keycode': line[3]
        }

new_dict = {}

for k,v in key_dict.items():
    if v['col'] in new_dict:
        new_dict[v['col']][v['row']] = {'key_name': k, 'keycode': v['keycode']}
    else:
        new_dict[v['col']] = {}
        new_dict[v['col']][v['row']] = {'key_name': k, 'keycode': v['keycode']}


pprint(new_dict)
