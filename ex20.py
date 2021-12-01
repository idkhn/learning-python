from sys import argv

script, input_file = argv # Collecting the filename

def print_all(f): # This function reads and prints the entire file
	print f.read()

def rewind(f): # Seek moves the read pointer to a place in the file, here to the start
	f.seek(0)

def print_a_line(line_count, f): # This function prints the line number (provided), then prints a single line (Note: the read pointer is on the next line, so when read() is used again it'll start from the next line.)
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file) # Using function here to pass the opened file

print "\nNow let's rewind, kind of like a tape."

rewind(current_file) # Rewinding to the start of the file

print "Let's print thress lines:"

# Simple counter and file variable pass to the line print function
current_line = 1
print_a_line(current_line, current_file)

current_line += 1 # incrementing the int variable
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)