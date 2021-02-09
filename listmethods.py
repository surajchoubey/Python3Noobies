numbers = [5,2,1,7,4]
print(numbers)
numbers.remove(5)
print(numbers)
numbers.append(20)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(7)) # is you enter 50 in numbers.index(50) its gonna throw in error to you
print(4 in numbers)
print(50 in numbers)
numbers.append(199)
print(numbers)

numbers2 = [5,2,1,5,7,4,5]

print(numbers2.count(5)) # count returns number of occurences

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers3 = numbers2.copy()
numbers3.append(58)
numbers2.append(69)
print(numbers2)
print(numbers3)

numbers4 = [5,2,6,4,6,1,4,8,6,9,8,9,4,3,2,4,2,3,6,3,7,8,5,3,4,1,5,1,6,7,3,4,1,4,0,1,1,0]

print(numbers4)

uniques = []

for number in numbers4:
    if number not in uniques:
        uniques.append(number)

print(uniques)