# an instance where you write a python code the code execute immediately before going to the next one is called repl(read, evvaluation, print, loop) eg;seen using your system cmd
# hence you can use your system cmd as calculator when you type in python firstly then follows by inputing the operations you want to perform using correct python syntax  
#let's says ;

a = 34
b = 2

# basic operatons using python operators;

print("a+b=", a+b) # addition operator
print("a-b=", a-b) # subtraction operator
print("a/b=", a/b) # division operator includes remainder in the answer
print("a*b=", a*b) # multiplication operato
print("a**b=", a**b) # power operator
print("a//b=", a//b) # floor division operator do not includes remainder after performing
print("a%b=", a%b) # modulus operator prints remainder of the number

# for comparison or conditional operators; comparison operators are operators that gives a true or force answer (boolen data type) 
# they includes:
# Operator	Meaning
# ==	Equal to # don't confuse = with ==, = assigns value to variable while == asks if a variable is equal to a particular value.
# !=	Not equal to
# >	Greater than
# <	Less than
# >=	Greater than or equal to
# <=	Less than or equal to
# examples

print(a>34) #false
print(a<34) #false
print(a>=34) #true
print(a<=34) #true
print(a!=34) #false
print(a==34) # is a equal to 34? #true

# logic operators;
# What are Logical Operators?
# Logical operators are used to combine multiple conditions.
# Think of them as answering questions like:
# Is this AND that true?
# Is this OR that true?
# Is this NOT true?

# Python has 3 logical operators:
# and
# or
# not

# 1️⃣ AND Operator
# Both conditions must be True.

print(True and True) #the answer is true (when writing true or false the first letter must be capitalise)
print(True and False) # the outcome is false
print(False and False) # the outcome is false
# Because both sides must be true.
# Real Example

age = 30
print(age > 18 and age < 40) #True

# Let's break it down:
# 30 > 18   # True
# 30 < 40   # True
# So:
# True and True
# Result:
# True

# 2️⃣ OR Operator
# At least one condition must be True.

print(True or False) #Output:True
print(False or False) #Output:False
# Because neither side is true.

# Real Example
print(10 > 20 or 10 < 20) #Output:True

# Because:
# 10 > 20   # False
# 10 < 20   # True
# So:
# False or True
# Result:
# True

# 3️⃣ NOT Operator
# Reverses the answer.

print(not True) #Output:False
print(not False) # Output:True

# Real Example

age = 30
print(not age > 40)

# Let's evaluate:
# age > 40
# Result: False
# Then: not False
# Result:True

# Truth Table (Memorize This)
# AND
# A	     B	    A and B
# True	True	True
# True	False	False
# False	True	False
# False	False	False
# OR
# A	     B	    A or B
# True	True	True
# True	False	True
# False	True	True
# False	False	False
# NOT
# A	  not    A
# True	    False
# False	    True

# Practice Task
# Predict the output before running:

print(10 > 5 and 20 > 10) #outccome: True

print(10 > 5 and 20 < 10) # outcome: False

print(10 > 5 or 20 < 10) #outcome: True

print(not 10 > 5) #False

print(not 10 < 5) #True

# Write your predictions first.

# Real-Life Example Based on Your Career
# Suppose you want to check whether you're on track for your goal.

python_skill = True
research_skill = True

print(python_skill and research_skill) #Output:True

# Meaning:
# You have both skills needed to move forward.

a+=3 # this updates the  outcome of a and save it in a hence 3 is added to the initial value of a and stores it back to a
print(a) 

# membership operators and identity operations will be discussed as we  progressed in later course.