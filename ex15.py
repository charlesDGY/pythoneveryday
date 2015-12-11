#this is an import code importing argv to this file
from sys import argv

#unpack the argv to script and filename
script, filename = argv

#open a file named filename
txt = open(filename)

#print the filename and the content of the file
print "Here's your file %r:" % filename
print txt.read()

#get the filename through the raw_input funciton
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
