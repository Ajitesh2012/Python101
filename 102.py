#Importing Modules
print("Importing modules")
print("\n")
import sys # system functions and parameters
from datetime import datetime
print(datetime.now())
def new_line():
    print('\n')
new_line()
from datetime import datetime as dt
print(dt.now())

def new_line():
    print('\n')
new_line()

# Advanced Strings
print("Advanced Strings")
my_name = "AJBGASDHASDASDASDAS"
print(my_name[0])# first Initial
print(my_name[-1])# Last Initials

sentence = "This is sentence."
print(sentence[:4])# first word
print(sentence[-9:-1])# Last word

# Splittting Sentence
print(sentence.split())
print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter.lower() in word.lower())#True
print()

too_much_space = "                Hello    "
print(too_much_space.strip())# to ignore space 

full_name = "AJ Rocks"
print(full_name.replace("AJ", "Ajitesh"))

movie = "Avengers"
print("Best movie is {}." .format(movie))

new_line()

#Dictionary
print("Dictionary are keys and volumes")
new_line
drinks = {"White_russians": 7, "Old fashion": 10}
print(drinks)
drinks.update({"White_russians" : 9})# updates values in dictionaries
print(drinks.get("White_russians"))
print(drinks)
employees ={"Finance": ["AJ", "DJ", "Rocket"], "SysAdmin": ["RTY", "YUI", "RTYU"]}
print(employees)
employees.update({"Sales": ["NMJ", "QAZ"]})
print(employees)

#List and Dictionaries
#List to dictionary
items = ["ball", "cake", "spoon", "plate"]
person = ["Rock", "Eat", "Wave", "Food"]
combined = zip(items,person)
item_dictionary = {key: value for key, value in combined}
print(item_dictionary)
new_line()
#run webserver in python
#python2 -m SimpleHTTPServer 80
#python3 -m http.server 80
#Ftp server
#python -m pyftpdlib -p 21 w
