# Variables need to start with a character, not a number
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Extra
import datetime
d = datetime.date.today()

print "Let's talk about %s." % name
print "He's %d inches tall." % height
# Some conversions here
print "Thats %d cms tall." % (height * 2.54)
print "He's %d pounds heavy." % weight
# ...and here.
print "Thats %d kilograms heavy." % (weight / 2.205)
print "Actually that's not too heavy."

print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this like is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %s." % (age, height, weight, age + height + weight)

# %s, %r, and #d are formatters
# %s = strings
# %d = numbers
# %x = convert an int value to hexadecimal number

# %r = in addition to returning the function, the value returned will also be shown
# 'print this no matter what'
print "d variable contains function and returned value: %r" % d
print "d otherwise would like like: %s" % d