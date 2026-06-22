# integers int - Integers are whole numbers that can be positive, negative, or zero. They do not have a decimal point. In Python, you can create an integer by simply writing a number without a decimal point.
# floats float - Floats are numbers that have a decimal point. They can also be positive, negative, or zero. In Python, you can create a float by writing a number with a decimal point or by using scientific notation (e.g., 1.5e2 for 150.0).
# strings str - Strings are sequences of characters enclosed in quotation marks (either single ' ' or double " "). They can contain letters, numbers, symbols, and spaces. In Python, you can create a string by enclosing text in quotes.
# booleans bool - Booleans represent truth values and can only be either True or False. They are often used in conditional statements and logical operations. In Python, you can create a boolean by using the keywords True or False.
# lists list - Lists are ordered collections of items that can be of different types. They are defined using square brackets [ ] and can contain elements separated by commas. In Python, you can create a list by enclosing items in square brackets.example: my_list = [1, 2, 3] or my_list = list([1, 2, 3])
# tupples tuple - Tuples are similar to lists but are immutable, meaning they cannot be changed after they are created. They are defined using parentheses ( ) and can contain elements separated by commas. In Python, you can create a tuple by enclosing items in parentheses.example: my_tuple = (1, 2, 3) or my_tuple = tuple([1, 2, 3])
# sets set - Sets are unordered collections of unique items. They are defined using curly braces { } and can contain elements separated by commas. In Python, you can create a set by enclosing items in curly braces or by using the set() function. example: my_set = {1, 2, 3} or my_set = set([1, 2, 3])
# dictionaries dict - Dictionaries are collections of key-value pairs. They are defined using curly braces { } and consist of keys and their corresponding values separated by a colon (:). In Python, you can create a dictionary by enclosing key-value pairs in curly braces. example: my_dict = {"key1": "value1", "key2": "value2"}  

#illustrations focus on the first four data types which are integers, floats, strings, and booleans. other data types will be covered in later lessons.

age = 30 # integer
print(age) # prints the integer value of age

#assuming that the data type of the variable is not known, we can use the type() function to check the data type of a variable in Python. The type() function returns the data type of the variable passed to it as an argument.
print(type(age)) # prints <class 'int'> indicating that age is an integer

height = 5.9 # float    
print(height) # prints the float value of height
print(type(height)) # prints <class 'float'> indicating that height is a float

name = "Iloka Chukwubuike Anthony" # string
print(name) # prints the string value of name
print(type(name)) # prints <class 'str'> indicating that name is a string

is_student = True # boolean. make sure to capitalize the first letter of True and False when defining a boolean variable in Python.
print(is_student) # prints the boolean value of is_student
print(type(is_student)) # prints <class 'bool'> indicating that is_student is a boolean