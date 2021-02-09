print("hello this is a multi line string")

#maths
print("\n")

print(50+50)
print(50-50)
print(50*50)
print(50/50)
print(50+50-50*50/50)
print(50**2)
print(50 % 6)
print(50 // 6)

print('\n')

#Variables & methods

print("Fun with Variables")
quote = "All is fair in love and war"
print(len(quote)) #length
print(quote.upper()) # uppercase
print(quote.lower())
print(quote.title())

name = "Heath"
age = 29 #int int(29)
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(29.9))

print("My name is " + name + " and I am " + str(age) + " years old ")

age += 1
print(age)

birthday =1 
age += birthday
print(age)

print('\n')

#Functions

print("Now, some functions")

def who_am_i():
    name = "Heath Ledger"
    age = 29
    print("My name is " + name + " and I am " + str(age) + " years old ")
    
who_am_i()

#adding in parameters
def add_one_hundred(num): 
    print(num+100)


add_one_hundred(100)

#adding in multiple parameters

def add(x,y):
    print(x+y)
    
add(7,8)

add(305,207)

#using return

def multiply(x,y):
    return x*y

def square_root(x):
    return x ** .5

print(int(square_root(64)))


#Boolean expressions (true or false)

print("Boolean expressions")

bool1 = True
bool2 = 3*3 ==9
bool3 = False
bool4 = 3*3 !=9

print(bool1,bool2,bool3,bool4)

print(type(bool1))

bool5="True"
print(type(bool5))

#relational and boolean operators

greater_than = 7>5
less_than = 5<7
greater_than_equal_to = 7>=7
less_than_equal_to = 7<=7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7>5) and (5<7)
test_or = (7>5) and (5<7)
test_not = not True

print(test_and,test_or,test_not)
print('\n')

# haha hmaverickadams

#Conditional Statements

print("Conditional Statements:")

def soda(money):
    if money >=2:
        return "You've got yourself a soda"
    else:
        return "No soda for you!"

print(soda(3))
print(soda(1)) 

def alcohol(age,money):
    if(age >= 21) and (money >=5 ):
        return "We're getting tipsy!"
    elif (age >=21) and (money < 5):
        return "Come back with money"
    else:
        return "You're too poor and too young!"
     
print('\n')     
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))           

#Lists
print("\nList have brackets:")
movies = [
    "When Harry met Sally",
    "The hangover",
   "The perks of being a wallflower",
    "The exorcist"
]

print(movies[0])
print(movies[0:100])

print(movies[:2])

print(movies[:1])
print(movies[1:])

print(movies[:-1])

print(len(movies))
movies.append("JAWS")
print(movies)
movies.pop()
print(movies)
movies.pop(1)
print(movies)

movies = [
    "When Harry met Sally",
    "The hangover",
    "The perks of being a wallflower",
    "The exorcist"
]
person = [
    "Heath Ledger",
    "Wade Wilson",
    "Leah Williams",
    "Jeff Bezos",
    "Randibaz"
]
print(movies)
print(person)

combined = zip(movies, person)

print(list(combined))

print(combined[0])

print(combined)

#Tuples

print("Tuples have parenthesis and cannot change")

grades= ("A","B","C","D","F")
# values of tuples do not change
print(grades[1])

#looping
print("For loops - start to finish of iterate:")

#for loops are from start to end


vegetables = ["cucumber","spinach","cabbage"]

for x in vegetables:
    print(x)
# for loops execute until statement is true
print("While loops  - Execute as long as they are true")

i=1
while i<=10:
    print(i)
    i+=1

print("Bye Bye I am signing out")