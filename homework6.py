# homework6.py Практическое задание по теме: "Словари и множества"
my_dict = {'Olga': 2001, 'Viktor': 1998, 'Ivan': 1995}
print('Dict:', my_dict)
print('Existing value:', my_dict['Olga'])
print('Not existing value:', my_dict.get('Lena'))
my_dict.update({'Egor': 2005, 'Mila': 2003})
a = my_dict.pop('Ivan')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
my_set = {1, 5, 5, 2, 3, 4, 3, False, False, 'Paul', 'Paul', 'PAUL', (7, 4, 3)}
print('Set:', my_set)
my_set.discard(2)
my_set.add(47)
print('Modified set:', my_set)
