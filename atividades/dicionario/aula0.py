d = {'kaua': 20, 'eduarda': 19, 'rodrigo': 21, 'ernani': 30}
new_d = {}
for person,years in d.items():
    new_d[person] = years
print(d,'\n',new_d,'\n\n\n')
new_d['kaua'] = 21
print(d,'\n',new_d)
