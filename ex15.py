# Importing module from sys library
from sys import argv

# Collecting the filename from the run arguments.
script, filename = argv
print open(filename).read()

# Saving the file to a variable.
txt = open(filename)

print "Here's your file %r: " % filename
# open() has functions that are imposed on the variable they're imported into, we use that here to read the file's contents and print it on screen.
print txt.read()

txt.close()

# Doing the same here, except we're collecting the filename during the running of the script.

# print "Type the filename again:"
# file_again = raw_input("> ")

# txt_again = open(file_again)
# print txt_again.read()