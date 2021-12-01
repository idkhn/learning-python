# Another method of collecting data
val = raw_input("Say something funny: ")
print(val)

# A method of collecting data
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)

# Difference between raw_input() and input() is the former stores everything as string, and the latter as whatever the input data happens to be

# Use control + c to terminate a program

# If any type of quote is entered in a raw_input() function, the function will escape the character so as to not prematurely stop collecting the whole input