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

print("my name is " + name + " i am " + str(age) + " Years old " + " i am " + str(height) + " cm tall. is " + str(is_student) + " that i am a student of python learning class")