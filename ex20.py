# from the system files import the argument vector library
from sys import argv

# unpack the varibles into the argv variable
# when starting the program we must pass it the name of a text file
script, input_file = argv

# creates a function with one argument that reads text from the file
def print_all(f):
	print f.read()
	
# rewind function definition
# seek with the argument 0 will return he file to its start	
def rewind(f):
	f.seek(0)

# this function prints a line	
def print_a_line(line_count, f):
	print line_count, f.readline(),
	
# variable holding the an open version of the passed file 	
current_file = open(input_file)

print "First let's print the whole file:\n"

# prints all lines in the test file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# after using the read function we want to go back to the start of 
# of the file, we can do that by using the seek function
rewind(current_file)

print "Let's print three lines:"

# starts the file on the first line
current_line = 1
# prints the first line
# current_line = 1
print_a_line(current_line, current_file)

# increments the current_line so that we can print the second
current_line += 1
# current_line = 2
print_a_line(current_line, current_file)

current_line = current_line + 1
#current line = 3
# prints the third line of the text file
print_a_line(current_line, current_file)

current_file.close()