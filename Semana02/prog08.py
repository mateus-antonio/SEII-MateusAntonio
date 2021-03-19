def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

print(hello_func('Hi', 'Mateus').upper())


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses,**info)

print(is_leap(2021))
print(days_in_month(2021,2))