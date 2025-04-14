from io import StringIO

# Create a StringIO object
output = StringIO()

# Write some data to the StringIO object
output.write('This is a test.\n')
output.write('This is only a test.\n')

# Get the string value of the StringIO object
print(output.getvalue())

# Close the StringIO object
output.close()

from io import StringIO

# Create a StringIO object with initial data
input = StringIO('Line 1\nLine 2\nLine 3\n')

# Read data from the StringIO object
print(input.read())  # Read all data

# Reset the cursor to the beginning of the StringIO object
input.seek(0)

# Read line by line
print(input.readline())  # Line 1
print(input.readline())  # Line 2
print(input.readline())  # Line 3

# Close the StringIO object
input.close()


