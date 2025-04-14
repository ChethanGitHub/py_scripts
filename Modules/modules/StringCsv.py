import csv
from io import StringIO

# Create a StringIO object
output = StringIO()

# Create a CSV writer object
csv_writer = csv.writer(output)

# Write some CSV data
csv_writer.writerow(['Name', 'Age', 'City'])
csv_writer.writerow(['Alice', 30, 'New York'])
csv_writer.writerow(['Bob', 25, 'Los Angeles'])

# Get the string value of the StringIO object
csv_data = output.getvalue()
print(csv_data)

# Close the StringIO object
output.close()

# Create a StringIO object with the CSV data
input = StringIO(csv_data)

# Create a CSV reader object
csv_reader = csv.reader(input)

# Read and print CSV data
for row in csv_reader:
    print(row)

# Close the StringIO object
input.close()