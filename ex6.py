# Using the formatter here, adding an integer to the string.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# A string in a string - 1
# Multiple formatters require perenthesis.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Another string in a string - 2x
print "I said: %r." % x
print "I also said: '%s'." % y

# Boolean value
hilarious = False
# Last string in a string - 1, total 4
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Adding two strings together to print both
print w + e