# Print String
print ("Hello World")
print ("Pentesting using python")
print ("Yoo this is fun")
print("This is "+"A string")

print ('\n') # new line

#Math in python
print("Math time")
print(50+50)#add
print(100-56)#subtract
print(50*63)#multiply
print(25/5)#divide
print(89/8)
print(50 + 50 -65 + 500 * 89)
print(50 ** 2)# exponents
print(50 % 6)# modulo
print(50 // 6)#numberwithout left overs


print ('\n') # new line

#Variables and Methods
print("Fun with variables")
quote = "All is fair in love and war"
print(len(quote))# length
print(quote.upper())
print(quote.lower())
print(quote.title())

name = "Heath"
age = 29 # int
gpa = 1.1 # float

print(int(age))
print(int(29.9))# doesnot round

print("My Name is " + name + "and I am " + str(age))

print ('\n') # new line

#Functions
print("Now, some functions")
def who_a_i():# defining functions
	name = "Aj"
	age = 30
	print("My Name is " + name + "and I am " + str(age))

who_a_i()

#adding in parameters
def add_one_hundred(num):
	print(num+100)
add_one_hundred(100)
print ('\n') # new line
#add in multiple parameters
print("using add")
def add(x,y):
	print(x+y)

add(7,7)
add(25,5)
print ('\n') # new line

#using return
print("using return")
def multiply(x,y):
	print(x*y)

add(7,7)
add(25,5)
print ('\n') # new line

#Boolean expressions(True or False)
print("Boolean expressions True or False ")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

print ('\n') # new line

#Relational and boolean operators
print("Relational and boolean operators")
greater_than = 7 > 5
lesser_than = 5 > 7
greater_than_equal_to = 7 >= 7
lesser_than_equal_to = 7 <= 7
print(greater_than,lesser_than,greater_than_equal_to,lesser_than_equal_to)

test_and = (7 > 5) and (8 < 7)
test_or = (7 >5) or (5 < 7)
true_not = not True
print(test_and,test_or)

print ('\n') # new line

#Conditional statements
print("Conditional statements")
def soda(money):
	if  money>= 2:
		return "Yo got urself soda"
	else:
		return "No sada for you"
print(soda(3))
print(soda(1))

print ('\n') # new line
print("alcohol and age Conditional")
def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We are getting tripsy"
	elif (age >= 21) and (money < 2 ):
		return "come back with more money"
	elif (age < 21) and (money >= 5):
		return "Nice Try kid"
	else:
		return "You to poor and young"

print(alcohol(20,1))
print(alcohol(19,5))
print(alcohol(21,5))

print ('\n') # new line

#List,Tuples,Looping
print("List,Tuples,Looping")
print("List have brackets")
movies = ["Avengers", "Batman", "Spiderman", "X-men", "AOE3"]

print(movies[1])
print(movies[0])
print(movies[-1])
print(movies[0:2])
print(movies[1:])# slicing
print(len(movies))
movies.append("Galaxy")# add item to list
movies.pop(3)#remove items from list
print(movies)

print ('\n') # new line
print("Pairng  two different List")
movies = ["Avengers", "Batman", "Spiderman", "X-men", "AOE3"]
person = ["Andy", "Beca", "Sarah", "Hercules", "Rio"]
combined = zip(movies, person)
print(list(combined))

print ('\n') # new line
print("Tuples in python")
print("Tuples have parenthesis(static) and cannot change")
grades = ("A", "B", "C", "D")
print(grades[1])

print ('\n') # new line
print("Looping Concept in python")
print("For loops - start to finish of itrate")

vegetables = ["potato", "spinach", "pizza", "cheese"]
for x in vegetables:
	print(x)
print ('\n') # new line
print("While loops as long as true")
i =1 
while i < 10:
	print(i)
	i += 1
print ('\n') # new line

#







