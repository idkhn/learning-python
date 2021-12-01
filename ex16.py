from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't ant that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# You use 'w' parameter to explicitly write to the file, r+ to read/write
target = open(filename, 'r+')
print target.read()

# --TIP-- We don't need to truncate if we use 'w', 'w+' or (see the decision tree file), 'r+' will append
# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "Now the file looks like this:"
target.seek(0)
print target.read()

print "And finally, we close it."
target.close()