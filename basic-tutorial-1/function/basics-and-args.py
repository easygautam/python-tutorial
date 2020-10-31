

# Lambda function to break line
l_break = lambda : print('')


# Function to add value of its two parameter
def add(a, b):
    return a + b


# Call fun add and print result
result = add(5, 8)
print(result)
l_break()

# Reference in function
def captilize(x):
    x.capitalize


# Test reference value change
name = 'Rahul'
captilize(name)
# Do not change the reference value because python create
# new object when we try to change reference value
print(name)
l_break()

# Default Argument
def sayMessage(message='Hello'):
    print(message)

# If we pass the value of the message then it will
# show passed message otherwise show 'Hello'


# On message pass
sayMessage('Hey how are you ?')  # Expected message 'Hey how are you ?'
l_break()

# If do not pass any message
sayMessage()  # Expected message 'Hello'
l_break()

# Keyword argument
def full_name(firstname, lastname):
    print(firstname + ' ' + lastname)


# Passing argument with keyword
full_name(lastname='Singh', firstname='Gautam')
l_break()

# Pass number of argument
def names(*names):
    for name in names:
        print(name, end=' ')


# Call names function
print('names() function called')
names('Gautam', 'Prashant', "Eduard", "N2", "N3", "\n")
l_break()

