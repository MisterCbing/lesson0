my_dict = {'Дмитрий': 1979, 'Марат': 1978, 'Анна': 1996}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Дмитрий'])
print('Not existing value: ', my_dict.get('Юрий'))
my_dict.update({'Юрий': 1992, 'Елена': 1999})
print('Deleted value: ', my_dict.pop('Марат'))
print('Modified dictionary: ', my_dict)

my_set = {3.14, 1, 2, 1, 'мандарин', 'Чебурашка', 3.14, 'мандарин'}

print()
print('Set:', my_set)
add_set = [(5, 6), 'Крокодил']
my_set.update(add_set)
my_set.remove('мандарин')
print('Modified set: ', my_set)