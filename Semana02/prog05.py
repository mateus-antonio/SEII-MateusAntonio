student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['name'])
print('')
print(student.get('age'))
print('')
print(student.get('phone','Not Found'))
print('')
student['phone'] = '555-5555'
print(student.get('phone','Not Found'))
print('')
del student['phone']
student.update({'name': 'Jane', 'phone': '555-5555'})
for key, value in student.items():
    print(key, value)