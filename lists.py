for item in 'Python':
    print(item)

for item in ['Mosh','John','Sarah']:
    print(item)

for item in [1,2,3,4]:
    print(item)

for item in range(10):
    print(item)

for item in range(5,10,2): # the third parameter is used to increase by running number by 2 each loop
    print(item)

prices = [10,20,30]
sum=0
for price in prices:
    sum+=price
print(f"Total {sum}")