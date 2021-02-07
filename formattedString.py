first = 'John'
last = 'Smith'
sentence = first + ' ['  + last + '] is a coder.'
msg = f'{first} [{last}] is a coder'
# the line above is a formatted string
print(msg)
print(sentence)

course = 'Python for beginners'
print(len(course))
# len helps us to take in limit input size

course = course.upper()
print(course.upper())
print(course.lower())

print(course.find('BEG'))

print(course.replace('BEGINNERS', 'Absolute Beginners'))
course = course.replace('BEGINNERS', 'absolute beginners')
print('PYTHON' in course) # Returns True
print('PYTHoN' in course) # Returns False
print(course)
print(course.title())


