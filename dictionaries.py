# a customer has name john smith email can be johnsmith@gmail.com and phone might be 1 2 3 4
# this is why we use a dictionary in python

customer = {
    "name":"John Smith",
    "age":30,
    "is_verified":True
}
customer["name"] = "Jack Smith"
print(customer["name"])
print(customer.get("birthdate","Jan 1 1980")) #Outputs none if no date mentioned just like this.
customer["birthdate"]="Jan 1 1980"
#print(customer["birthdate"]) it throws an error
print(customer)

#########################################################

#exercise for me

phone_number = input("Enter your phone number: ")
number_names = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}


phrase = ""
for x in phone_number:
    phrase = phrase + number_names[x] + " "

print(phrase)

######################-MOSHS-SOLUTION-###############################

phone = input("Phone: ")
digits_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}

output = ""

for ch in phone:
    output += digits_mapping.get(ch, "!") + " " # in (ch,"!") it will supply "!" to the default value

print(output)

"""
Enter your phone number: 12352346
One Two Three Five Two Three Four Six 
Phone: 98123
! ! One Two Three 
"""