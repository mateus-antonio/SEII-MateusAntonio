import prog09_module as mm
from prog09_module import find_index as fi
import sys
import random
import math

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses,'Math')
print(index)
index = fi(courses,'History')
print(index)

print(sys.path)

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)