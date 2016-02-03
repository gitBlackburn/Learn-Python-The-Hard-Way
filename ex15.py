# uses argv from the sys lib
# adds arguments 
# from sys import argv

# # two arguments scripts and filename
# script, filename = argv

# # opens the text file and stores it in txt
# txt = open(filename)

# # notifies the user
# print "Here's your file %r:" %filename
# # reads the text file
# print txt.read()

# prompts the user for more action
print "Type the file name again:"
# stores the usrs imput in file_again
file_again = raw_input("> ")

# i think that this makes a references to txt
txt_again = open(file_again)
# shows the users the txt file again
print txt_again.read()

#txt.close
txt_again.close()