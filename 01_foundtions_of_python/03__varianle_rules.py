#rules of defining variables in python
#1. Variable names must start with a letter (a-z, A-Z) or an underscore character (_).
#2. Variable names cannot contain spaces.
#3. Variable names can contain letters, numbers, and underscores, but they cannot start with a number. For example, valid variable names include my_variable, variable1, and _myVariable. Invalid variable names include 1variable (starts with a number) and my variable (contains a space).
#4. Variable names are case-sensitive.(age and Age are two different variables)
#5. Variable names cannot be the same as reserved keywords in Python.(e.g., if, else, while, for, def, class, etc. are reserved keywords and cannot be used as variable names)

# 34age = 34  # This is an invalid variable name because it starts with a number.
age34 = 34  # This is a valid variable name because it starts with a letter and contains numbers.
age = 34    # This is a valid variable name because it starts with a letter and contains only letters.
_age = 34   # This is a valid variable name because it starts with an underscore and contains only letters.
# age$ = 34   # This is an invalid variable name because it contains special characters ($).