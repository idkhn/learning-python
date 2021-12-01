cars = 100
# floating point integer
space_in_a_car = 4.0
drivers = 30
passengers = 90
# using variable values to perform calculations
cars_not_driven = cars - drivers
# copying the value of one variable to another
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Example variables to perform a calculation later
i = 1
x = 2
j = 3

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Perform calculation during print
print i + x + j

# If in line #11 the variable was 'passenger' instead of the plural, an error would occur
# A floating point integer is unnecessary for people, people don't come in fractions

# A single = assigns value, and a double == performs a true/false check on either side.
# Use spaces between variables and their values, it's good form.