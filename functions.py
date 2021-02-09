# functions are used to organize our code in better manner

def greet_user(first_name="Pussy",last_name="Master"):
    print('Hi there! ' + first_name + " " + last_name)
    print('Welcome aboard ' + first_name + " " + last_name)


print("Start")
greet_user(first_name="John",last_name="Smith")
greet_user("Mary")
greet_user("")
greet_user()
# calc_cost(total=50, shipping=5, discount=1) you can write this way to improve the readability of the code
print("Finish")