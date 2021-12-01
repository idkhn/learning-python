# We're creating a function that takes two arguments. They're then printed by the function.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) # We directly provide the arguments in the call

print "OR we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # We can pass variable values to the function

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) # Same as numbers, but also doing math

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # Mix of variables, math, and numbers

def flights(departures, layovers):
	print "You had %d flights, with %d layovers, so you likely had to board a plane at least %d times!" % (departures, layovers, departures + layovers)

departures = 12
layovers = 3
flights(2, 0)
flights(12 - 5, 10 + 10)
flights(departures, layovers)
flights(departures - 2, layovers + 3)
flights(-1, 4)
flights(0, 1)
departures = int(raw_input("How many flights did you take last month? "))
layovers = int(raw_input("Any layovers? "))
flights(departures, layovers)