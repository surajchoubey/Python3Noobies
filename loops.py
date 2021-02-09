i = 1;

while i<=10:
    print('*'*i)
    i+=1
print("Done")


# while loop to building a guessing game
flag = True
number = 6
geez=0
i = 1

while flag and i <=3:
    geez = int(input("Your guess is: "))
    if geez == number:
        flag=False
    i+=1

if not flag:
    print("Congratulations you won the guessing game")
else:
    print("Go home you pussyheads")
