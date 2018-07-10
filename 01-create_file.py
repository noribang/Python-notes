# Reference: http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#            http://www.pythonforbeginners.com/cheatsheet/python-file-handling

# Create .txt file and make it writeable.
file = open("testfile.txt", "w")

# Write lines of text to file.
file.write("Hello World.")
file.write("This is our new text file")
file.write("and this is another line.")
file.write("Why? Because we can.")

# Close file.
file.close()

# Open file and read contents.
readFile = open("testfile.txt", "r")

# Read file and print.
print readFile.read()