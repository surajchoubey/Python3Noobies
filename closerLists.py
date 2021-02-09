names = ['John','Bob','Mosh','Sarah','Mary']

names[0] = 'Jon'

print(names[2:5])

print(names)

numbers = [1,2,14,4,5,6,7,7,13]

largest = numbers[0]

for i in numbers:
    if largest < i:
        largest = i

print(largest)