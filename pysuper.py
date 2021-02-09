#Importing
print("Importing is important:")

import sys #system functions and parameters
# sys is needed to exit out

from datetime import datetime
print(datetime.now())


# this is called importing with an alias
from datetime import datetime as dt
print(dt.now())

def new_line():
    print('\n')
    
new_line()

#Advanced Strings

print("Advanced Strings:")

my_name = "Heath"
print(my_name[0]) # printing first letter
print(my_name[-1]) # printing last letter

sentence = "This is a sentence."

print(sentence[:4]) # printing first word 
print(sentence[4:])

print(sentence[-9:-1]) # first word
print(sentence[:-8]) #last word

print(sentence[-0:])

#we want to split sentence inot words

print(sentence.split())
sentence_split = sentence.split()
sentence_join = " ".join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))
new_line()
quoteception = "I said, 'give me all the money'"

print(quoteception)

quotecept="I said, \"give me all the money\""
print(quotecept)

print("a" in "Apple")
letter ='A'
word ="Apple"
print(word)
print(letter in word.lower())  # Improved case - sensitive

#this is just a demostration

word_2 = "Bingo"
print(word_2.lower())
print((letter.lower() in word.lower()) and not(letter.lower() in word_2.lower()))

too_much_space = "         hello        " 

print(too_much_space)

print(too_much_space.strip())

full_name= "eath Adams peath"
print(full_name.replace("eath" , "Heath"))

new_line()
print(full_name)
print(full_name.find("Adams"))

#Placeholders

movie = "The hangover"

# old school method
# print("My favorite movie is " + movie)

print("My favorite movie is {}.".format(movie))

def favorite_book(title, author):
    fav="My favorite book is \"{}\", which is written by {}. " .format(title,author) 
    
    return fav

# now we can print our favorite book

print(favorite_book("The Great Gatsby" , "F. Scott Fitzgerald"))

new_line()

#Dictionaries
print("Dictionaries are keys and values basically:")

# so in the past we have used list[] , tuples() , Dictionaries{}

drinks = {"White Russians": 7, 
          "Old Fashion": 10,
          "Lemon Drop": 8,
          "Buttery Nipples": 6}
# drink is the key, and price is the value
# white russians is the key and 7 is the value

print(drinks)

new_line()

employees = { "Finance": ["Bob", "Linda" , "Tina"] ,
                "IT" : ["Gene" , "Louise" , "Teddy"],
                "HR" : ["Jimmy Jr", "Mort"] }

print(employees)

employees['Legal'] = ["Mr. Frond"] # add new key : value pair

print(employees)

employees.update({" Sales" : ["Andie", "Ollie"]})

print(employees)

# we saw couple of different ways
# updating price of white russians drink
drinks["White Russians"] = 8

print(drinks)

print(drinks.get("White Russians"))

# if we try to print something which is not there in the list
print(drinks.get("White Randis"))
print(drinks.get("Martini"))

print(drinks["White Russians"])

print(employees["IT"])

movies = ["When Harry Met Sally" , "The hangover" ,"The Perks of being a Wallflower", "The Exorcist"]

person=["Heath","Bob","Leah","Jeff"]

combined = zip(movies,person)

movie_dictionary = {key: value for key, value in combined}

print(movie_dictionary)




