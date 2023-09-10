# using file
file = open("sample.csv","r")
print(file.read())
file.close()

# using csv package
import csv

with open("sample.csv","r") as data_file:
    sample_data = csv.reader(data_file)
    for row in sample_data:
        if row[0] != "Adelaide":
            print(row[0])

# using pandas package
import pandas as pd

data = pd.read_csv("sample.csv")
print(data)

print(data['Adelaide'])