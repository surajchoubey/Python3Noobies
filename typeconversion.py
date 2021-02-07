"""

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
#int() float() bool() these can convert the types
print(type(age))
print(age)



weight_lbs = input('Weight (lbs):')
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)

course=('Python course for "Beginners"')
another=course[:]

print(course)
print(course[0])
print(course[1])
print(course[-1])
print(course[-2])

print(course[0:4])
print(course[0:])
print(course[5:])
print(course[:-7])
print(course[:])

print(another)

"""

name= 'Jennifer'

print(name[1:-1])