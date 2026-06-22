#A variable is a named storage box in Python. It holds data you can reuse, change, and combine.
#You can create a variable by assigning a value to it using the equals sign (=).
#variable can be an interger, a float, a string, or even a boolean value (True or False).
#Here are some examples of variables in Python:
#  codes below

name = "Iloka Chukwubuike Anthony" #string variable. quotation marks are used to define a string variable
age = 30 #integer variable
height = 5.9 #float variable containing decimal number
is_student = True   #boolean variable tue or false value
field_of_study = "computational Biology" #string variable
Goal = "to solve real-life issues in health, connectivity, and finance in Africa" #string variable
#code to print the variables that we have created by assigning a value to them. we can print the variables by using the print() function and passing the variable name as an argument.
print(name)
print(age)
print(height)
print(is_student)
print(field_of_study)
print(Goal)
print("my name is " + name + " and I am " + str(age) + " years old" + " iam learning " + field_of_study + " and my goal is " + Goal)

#code evalautions and corrections

# string variables can be combined using the + operator, and you can convert other data types to strings using the str() function.
# we will see the modern way of writing combination of string variables and other data types in the next lesson on f-strings in python.
# #str(age)
# Python programmers usually use lowercase variable names:
# goal = "..." instead of Goal, and field_of_study instead of Field_of_study. This is a convention that makes code easier to read and understand.

#Python cannot directly join text and numbers: that's why we use str() to convert the number to a string before concatenation. For example, str(age) converts the integer age to a string so it can be combined with other strings.
#Concatenation means joining things together. In Python, you can concatenate strings using the + operator. For example:

first_name = "Iloka"    
last_name = "Chukwubuike"   
full_name = first_name + " " + last_name
print(full_name)    
print(first_name + last_name) # This will print "IlokaChukwubuike" without a space in between.
print(first_name + " " + last_name) # This will print "Iloka Chukwubuike" with a space in between.)

print("uppercase:", full_name.upper())  # Converts the string to uppercase
#comma is used to separate items in the print function, and it automatically adds a space between them. So, when you use a comma, you don't need to worry about adding spaces manually. For example:
print("my name is", name, "and I am", age, "years old")  # This will print with spaces between the items.
print("uppercase:" + full_name.upper()) #the plus sign (+) is used to concatenate strings, but it does not add spaces automatically. So, if you use the + operator, you need to make sure to include spaces where necessary. For example:
print("my name is " + name + " and I am " + str(age) + " years old")  # This will print without spaces unless you add them manually.
#to print with spaces between the items, you can use either the comma or the + operator, but you need to be mindful of how they handle spaces. The comma will automatically add spaces, while the + operator requires you to add spaces manually.
#add space manually when using the + operator, like this:
print("my name is " + name + " and I am " + str(age) + " years old")  # This will print with spaces between the items.
#where is the space? the space is added manually by including a space character (" ") in the string concatenation. For example, "my name is " + name + " and I am " + str(age) + " years old" includes spaces before and after the variable name and age to ensure that the final output has spaces between the words.
#the space will not be added if you forget to include it in the string concatenation. For example, if you write:
print("my name is" + name + "and I am" + str(age) + "years old")  # This will print without spaces between the items.
#In this case, the output will be "my name isIloka Chukwubuikeand I am30years old" without any spaces between the words. So, it's important to remember to include spaces when using the + operator for string concatenation to ensure that your output is formatted correctly.
print("uppercase:", full_name.upper()) 