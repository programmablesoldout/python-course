
# escape sequence characters are use to include special characters to string
# some of the common escape sequence characters includes:

# \n any text after the newline character is printed on the next line

print("Hello\nWorld") #Hello is printed on first line and world is printed on second


# \\ double backslash prints one backslash  and a single backslash prints single slash. try adding more slash and predict

print("He said \"Hello\"") # the line will prints He said "Hello" because double quote escape sequence charcter is inserted before Hello and after

# \t it is use to insert tab (a long space in writing)

print("Name\tAge") #after the name is displayed long space follows before Age is displayed on the screen

# \' adds a single quotes wherever it appears

print('It\'s Python') #the line of code wil prints It's python single quotes appears where the symbol appears

print("it's python")

print ("it\'s python") # the result of 18 20 and 22 are the same 20 and 22 works cos of the use of sepearte quotes the double and the single.
#but on 18 we must use escape sequence character in other not to confuse python
# \" adds a double quotes wherever it appears
# same method can be applied to example in line 12

# let's try it
print('He said "hello"')

# let's consider special characters used in print statements to add special chracters:(sep and end)
# by default adding a comma to a print statement automatically add space to it to override that we use
# special print varaible called seperator represented by sep=""  it automatically add any special characters within the double quotation any where comma (,) is in the print statement


print("Iloka", "Anthony", 30) # outcome is Iloka Anthony 30 where the , automatically add space to it


print("Iloka", "Anthony", 30, sep=" ") # here each argument within the print statement are ended with , and within the quotation of sep= nothing was added and then the function of , was removed but not replaced

print("Iloka", "Anthony", 30, sep="-") # sep="-" at the end of the code adds - to every seperator except the seperator at the end that do not have any more words

# for end statement represented by end="" this adds any character to the ending part of print argument and  then joins them in one line
# python by default esecute code line by line but the end statement is used to manipulate that  to print word in one line
# illustrations:

print("Hello")
print("World")
# this is printed one after another in 2 line as
# hello
# world. hence to manipulate that into displaying the outcome on one line lets use the end speacial print features;

print("Hello", end ="") # with no space in between the end qoutation mark
print("World")

# the line of code at 54 and 55 will print helloworld on display the , at the ending part is remove and then it presents the outcome in a single line additio n of space in the outcome when using sep and end is added manually since , is manupulated
# more examples;

print("Hello", end =" ") #with space between the end quotation it added space at the end of the Hello brfore joining.
print("World")

print("Python", end=" -> ")
print("AI")
# observe that when there is a space between quotation mark of the sep and end statement it also observe and it is also not obcerve when it is not introduced correctly. 

# lets now use both of them simulteneously
print("Name", "Age", "Field", sep=" | ", end=" => ")
print("Anthony")


# 💡 Professional Tip

# As a beginner, you'll mostly use:

# print("Hello", name)

# or

# print("Hello " + name)

# Later, you'll mostly switch to f-strings, which are cleaner:

# print(f"Hello {name}")

# For now, just remember:

# sep = what goes between items.
# end = what goes after the print statement and joins 2 line.

# That's the mental model most programmers use. 🚀

# At your current level, you now understand:

# print()
# Strings
# Numbers
# Variables
# Comments
# Concatenation
# Type Casting
# Escape Sequences
# sep
# end
# input()
# congratulations
# You're building a solid foundation. The next big leap is making programs think using if, elif, and else.