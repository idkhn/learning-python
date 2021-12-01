# The one line version

from sys import argv

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())

# We don't .close() here but probably not necessary as no files are assigned a variable (they're manipulated directly)