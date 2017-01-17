# imposts argv from sys module
from sys import argv

# splits argv into variables
script, input_file = argv

# defines fx to read and print the arg
def print_all(f):
	print f.read()

# defines fx to go back to line 0 in arg file
def rewind(f):
	f.seek(0)

# defines fx to show the line number and read/print that line from arg
def print_a_line(line_count, f):
	print line_count, f.readline()

# opens the arg into variable
current_file = open(input_file)

print "First let's print the whole file:\n"

# uses print_all fx to print current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# uses rewind fx to go back to line 0 in current_file
rewind(current_file)

print "Let's print three lines:"

# sets counter to 1
current_line = 1
# prints the line counter and the line corresponding to that number
print_a_line(current_line, current_file)

# increments line counter and repeats the print of corr number
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
