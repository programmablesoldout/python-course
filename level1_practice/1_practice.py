'''Q1: Your First Program

Write a program that prints: 
Hello, World! Welcome to Python.
'''

print("Hello, World! Welcome to Python. ") #solution make sure the capitalise words and comma are where they are meant to be


'''Q2: Print a Poem

Write a program that prints the following poem using a single statement: 
Twinkle, twinkle, little star, 
How I wonder what you are!

(Hint: Use \n for a new line.)
'''
print("Twinkle, twinkle, little star, "  "\nHow I wonder what you are!") # method1

print('''Twinkle, twinkle, little star,
How I wonder what you are!''') # method 2

print("Twinkle, twinkle, little star, \nHow I wonder what you are!") #method 3

'''Q3: Variables & Data Types

Create variables to store: - Your name (string)
-	Your age (integer)
-	Your height in meters (float)
-	A boolean value representing whether you are a student Print all of them in one line.
'''
name = "Anthony"
age = 26
height = 157.6
is_student = True

print("my name is " + name + " i am " + str(age) + " Years old " + " i am " + str(height) + " cm tall. is " + str(is_student) + " that i am a student of python learning class") # solutions
'''
Q4: Typecasting Practice

You are given a string: num = "45"

Convert it into an integer and add 10 to it. Print the result.
'''
num = "45"
print (int(num) + 10 )

'''Q5: Taking User Input

Write a program that:
1.	Asks the user for their favorite food.
2.	Prints: Wow! I also like <food>.

'''
food = input("What's your favorite food?\n")
print("Wow i also like " + food )

'''Q6: Simple Calculator

Write a program that:
1.	Takes two numbers as input from the user.
 
2.	Prints their sum, difference, product, and quotient.
'''

first_number = int(input("Enter first number?\n"))
second_number = int(input("Enter second number?\n"))
print("a + b =", first_number + second_number)
print("a - b =", + first_number - second_number)
print("a * b =", + first_number * second_number)
print("a / b =", + first_number / second_number)
print("a // b =", + first_number // second_number)
print("a % b =", + first_number % second_number)

'''Q7: Escape Sequences

Print the following output using escape sequences: 
Harry said, "Python is awesome!" This is on a new line.
This is a tab ->	<- here
'''

print("Harry said, \"python is awessome!\" \nThis is on a new line.\nThis is a tab ->\t<-here" )

'''Q8: Operator Challenge

Write a program that:
1.	Takes an integer as input from the user.
2.	Prints the square and cube of that number.

'''
a = int(input("Enter an integer\n"))
print("a**2 =", a**2)
print("a**3 =", a**3)

'''Q9: Quick Quiz (True/False)

Mark True or False:
1.	Python code must always end with a semicolon: False
2.	# The	symbol is used for comments in Python: True
 
3.	"123" and 123 are the same in python: False
 
4.	The * operator is used for multiplication: True

5.	\n creates a new line: True
 
6.	Variables in Python can start with numbers: False
7.	int("10") + 5 gives 15 : True
'''