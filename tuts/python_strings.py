# simple string
greeting = "hello "
print(greeting)

# multiple line string
some_text = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(some_text)

# formatted string
name = "John Doe"
greeting += f' this is {name}' 
print(greeting)

# accessing strings

first_letter = greeting[0]
last_letter = greeting[-1]
middle_letter = greeting[len(greeting)//2]

print("the first letter "+ str(first_letter))
print("the last letter %s "% (last_letter))
print("the last letter {} ".format(middle_letter))

# slicing a string

# first half
print("first half "+greeting[len(greeting) // 2 :])
# second half
print("second half " + greeting[: len(greeting) // 2])
# in between
print("in between " + greeting [5:9])


print("the result is"+greeting[0])  # first character
print("the result is"+greeting[-1])  # last character
print("the result is"+greeting[0:3])     # characters from 0 to 2
print("the result is"+greeting[2:])      # characters starting from 2
print("the result is"+greeting[:-2])     # all but the last two characters
another_text = "Hello, World!"
print(another_text[-5:-2])              #reverse slicing
print("the result is"+greeting[1::2])       # every other character, starting from index  1

# string operations
capitalized_greeting = greeting.upper()    # convert to upper case
print('Capitalized Greeting: ', capitalized_greeting)

lowercase_greeting = greeting.lower()        # convert to lower case
print('Lowercase Greeting: ', lowercase_greeting)
# capitalizing first letter of each word
title = "the quick brown fox"
print("Title Case: ", title.title())

# check if something exists in a string
print('Number of letters in Greeting: ', len(greeting))         # number of characters in a string

greeting = "Python is an interpreted programming language and Ruby is another one as well"
formatted_greeting = greeting.replace('Python','Ruby')                   # replace substring
print('Formatted Greeting: ', formatted_greeting)

# checking if a string contains another string
has_python = 'Python' in greeting               # True or False
print('Does it contain Python? ', has_python)

starts_with_hello = greeting.startswith('Hello')          # True or False
print('Starts With Hello? ', starts_with_hello)

ends_with_world = greeting.endswith('World')              # True or False
print('Ends With World? ', ends_with_world)

# finding specific strings in a text
index_of_space = greeting.find(' ')                # position of the space character
print('Index of Space: ', index_of_space)

last_index_of_space = greeting.rfind(' ')           # position of the last occurrence of the space character
print('Last Index of Space: ', last_index_of_space)

print("python is found at the  index :", greeting.index('python'))      # gives the first occurance of python
greeting = "Python is an interpreted programming language and Ruby is another one as well, but python is more popular"
print("python is found at the  index(reverse) :", greeting.rindex('python'))      # gives the last of python
# using split method to break up strings into lists based on a delimiter (default is white space)

words = greeting.split()

print("Words list:", words)

# join method which takes a sequence and joins them into one string with a specified separator (default is white space)
sentence = "This is a sentence."

# using split with a different delimiter

parts = sentence.split(".")

print("Sentence parts:", parts)

# stripping from unwanted characters
junk = "<html><body>Spam eggs</body></html>"
cleaned = junk.strip("<html><body>")             # removes leading and trailing characters
print("Cleaned Junk: ", cleaned)

