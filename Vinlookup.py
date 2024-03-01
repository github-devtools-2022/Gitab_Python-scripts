#!/usr/bin/env python3

import sys
import csv

# Check if both CSV files are provided as arguments
if len(sys.argv) != 3:
    print("Usage: {} <Email.csv> <Vir-project-user-email>".format(sys.argv[0]))
    sys.exit(1)

# Assign filenames to variables
EMAIL_CSV = sys.argv[1]
VIRI_CSV = sys.argv[2]

# Function to read CSV files and create a dictionary
def read_csv(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data[row[0]] = row[1]
    return data

# Read Email.csv and create a dictionary of usernames and emails
email_data = read_csv(EMAIL_CSV)

# Check if both files exist
try:
    with open(VIRI_CSV, 'r') as viri_file, open("output.csv", 'w', newline='') as output_file:
        reader = csv.reader(viri_file)
        writer = csv.writer(output_file)
        for row in reader:
            # Check if username exists in the dictionary
            if row[10] in email_data:
                row[12] = email_data[row[10]]  # Assign the email to column 13
            else:
                row[12] = "NA"  # Assign "NA" if no match is found
            writer.writerow(row)  # Write the updated row to the output file
except FileNotFoundError:
    print("Error: One or both input files do not exist.")
    sys.exit(1)