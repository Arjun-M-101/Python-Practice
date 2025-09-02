# For reading csv files easily import csv module
import csv

with open("input_file.csv","r") as file:
    reader=csv.DictReader(file) # This reads the csv file as a dictionary
    # Now we can access the columns by their header names
    for row in reader:
        print(row["age"]) # Print the age column, which is the age column
        
# If they ask not to use csv module, then we can use the following code
with open("input_file.csv","r") as file2:
    rows= file2.readlines()  # Read all lines from the file as rows
    for row in rows[1:]:  # Skip the header row
        columns = row.strip().split(",") # Split each row into columns
        print(columns[2])  # Print the age column, which is the age column