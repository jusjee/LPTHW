# Tells python to import the argv module, what is 'from sys'?
from sys import argv

# Breaking up argv into variables
script, filename = argv

# The file with 'filename' is now stored into the variable 'txt'
txt = open(filename)

# Printing message
print "Here's your file %r:" % filename
# Reading and printing the contents of the txt variable (opened filename)
print txt.read()
txt.close()

# Doing the same thing again, but changed filename to 'file_again'
# This uses an input rather than an argument
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
