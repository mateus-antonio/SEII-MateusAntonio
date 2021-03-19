# Mutével
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
list_1.insert(0,'English')

print(list_1)
print(list_2[2:4])

for num, curso in enumerate(list_1, start=1):
    print(num, curso)


# Immutável
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci','Math'}
art_courses = {'History', 'Math', 'Art', 'Design','English'}

print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.difference(art_courses))
print(cs_courses.intersection(art_courses))
print(cs_courses.union(art_courses))


# Listas vazias
empty_list = []
empty_list = list()

# Tuples vazios
empty_tuple = ()
empty_tuple = tuple()

# Sets vazios
empty_set = {} #Não é certo
empty_set = set()