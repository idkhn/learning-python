# Importing argv modules from the sys library
from sys import argv

script, first, second, third = argv
# If you don't enter the required arguments you'll get an error about only providing x number of values not being enough.
# argv stores values as strings, you'll need to typecast the string value to change it to something else, eg int(first)

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

fourth = raw_input("Offer a fourth variable: ")
print "Your fourth variable is:", fourth