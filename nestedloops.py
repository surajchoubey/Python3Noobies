for x in range(4):
    print(x)

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

print("This ends here!")

numbers = [5,2,5,2,2]

for i in numbers:
    print('X'*i)

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)