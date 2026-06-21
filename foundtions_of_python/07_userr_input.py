# usser input is represented by input function; input()
# it is use for taking user information
# it is important to use input prompt to communicate effectively with the user and predict the outcome of data.

# illustrations 1 showing how to take users name and displaying it on the screen.

name = input("What is your name? ")
print("Hello " + name) #concatenation using + and observing addition of space manually
#or
# print("Hello",name) #concatenation using , to add space automatically

# illustration 2 showing how to typecast when taking numbers that are strings and using them to make calculations

a = input("Enter first number ") # the input gotten is string confirm with print(type(a))

b = input("Enter second number ") # the input gotten is string confirm with print(type(b))

print (a + b, "wrong") # trying to add this two string will result to wrong answer cos python will concatenate as string giving joining of the 2 numbers

# to correct perform mathematical operation of the two number the string will be converted to integer so that python can perfporm calculation correctly.

# basic typecast method to solve the problem
a = input("Enter first number ")
a = int(a) # this line convert the gotten input which is string and convert it to integer and store it in variable a
b = input("Enter second number ")
b = int(b) # this line convert the gotten input which is string and convert it to integer and store it in variable b
print(a + b,"correct but basic approach")

# more standard typecast
a = int(input("Enter first number ")) # here the code takes the string input and immediately converts to integer with just one line of code
b = int(input("Enter second number")) # similar to above code
print(a + b, "Correct")

# run the code and enjoy having fun with it.