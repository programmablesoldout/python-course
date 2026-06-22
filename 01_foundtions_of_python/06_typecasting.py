#type casting is changing one data type to another.
#build in function like int(), float(), str(), and bool() can be used to convert data types in Python. 
#typecasting is useful to before performing operations that require specific data types, such as mathematical calculations or string concatenation. For example,

age = 30 # integer
print(age) # prints the integer value of age
print(type(age)) # prints <class 'int'> indicating that age is an integer

#to convert age from an integer to a string, we can use the str() function:

a = str(age) # this will convert the integer value of age to a string and assign it to the variable a
print(a) # this will print the string value of a which is "30"
print(type(a)) # this will print <class 'str'> indicating that a is now a string

Age = "30" # string
print(Age) # prints the string value of Age
print(type(Age)) # prints <class 'str'> indicating that Age is a string 

#to convert Age from a string to an integer, we can use the int() function:

b = int(Age) # this will convert the string value of Age to an integer and assign it to the variable b
print(b) # this will print the integer value of b which is 30
print(type(b)) # this will print <class 'int'> indicating that b is now an integer  

price = "2000" # string
print(price) # prints the string value of price
print(type(price)) # prints <class 'str'> indicating that price is a string

# float() can be used to convert a string or an integer to a float. For example:

c = float(price) # this will convert the string value of price to a float and assign it to the variable c
print(c) # this will print the float value of c which is 2000.0
print(type(c)) # this will print <class 'float'> indicating that c is now a float  

# to convert to a boolean, we can use the bool() function. For example:

is_valid = 0 # integer
print(is_valid) # prints the integer value of is_valid which is 0
print(type(is_valid)) # prints <class 'int'> indicating that is_valid is an integer

# boolean conversion

d = bool(is_valid) # this will convert the integer value of is_valid to a boolean and assign it to the variable d
print(d) # this will print the boolean value of d which is False
print(type(d)) # this will print <class 'bool'> indicating that d is now a boolean 

is_studdent = "" # empty string
print(is_studdent) # prints the string value of is_studdent which is an empty string 
print(type(is_studdent)) # prints <class 'str'> indicating that is_studdent is a string

# boolean conversion of an empty string will result in False, while any non-empty string will result in True. For example:

e = bool(is_studdent) # this will convert the empty string value of is_studdent to a boolean and assign it to the variable e
print(e) # this will print the boolean value of e which is False    
print(type(e)) # this will print <class 'bool'> indicating that e is now a boolean 

learning_python = 1 #integer
print(learning_python) # prints the integer value of learning_python which is 1
print(type(learning_python)) # prints <class 'int'> indicating that learning_python is an integer

# to convert the integer above to boolean.

f = bool(learning_python) # this will convert the integer value of learning_python to a boolean and assign it to the variable f
print(f) # this will print the boolean value of f which is True
print(type(f)) # this will print <class 'bool'> indicating that f is now a boolean

# Why Type Casting Matters

# Imagine you're building a finance app.

# salary = "500000" string
# bonus = "100000"  string

# If you do:

# print(salary + bonus)

# Output:

# 500000100000

# Python joins the text.

# But if you convert them:

# print(int(salary) + int(bonus))

# Output:

# 600000 Now Python performs actual mathematics.
