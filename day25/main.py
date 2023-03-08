"""using csv, pandas library for file"""

# import csv
import pandas
CSV_FILE = r"c:\Users\Olalekan\Desktop\Python\Angela_Yu\day25\weather_data.csv"

# with open(CSV_FILE) as data_file:
#     data = data_file.readlines()
#     print(data)

# with open(CSV_FILE) as data_file:
#     csv.reader(data_file)
#     temperature = []
#     for row in csv.reader(data_file):
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

data = pandas.read_csv(CSV_FILE)
print(data["temp"])