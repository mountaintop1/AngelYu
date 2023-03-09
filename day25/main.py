"""using csv, pandas library for file"""

# import csv
import pandas

CSV_FILE = "./AngelYu/day25/weather_data.csv"

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

# data = pandas.read_csv(CSV_FILE)
# data_dic = data.to_dict()
# condition = data.condition.str.lower()
# print(condition)
# print(data_dic)
# print(data["temp"])
# print(data["temp"].to_list())
# print(data["temp"].max())
# print(data["condition"])
# print(data["temp"].mean())

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

#monday = data[data.temp == data.temp.max()]
# condiftion = monday.condition
# print(condiftion)

# data_dict = {"students": ["Amy", "James", "Angela"],'scores': [76, 56, 65]}

# data1 = pandas.DataFrame(data_dict)
# print(data1)
# data1.to_csv("AngelYu/day25/new_data.csv")

central_park_file = "./AngelYu/day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

# gray, cinnamon, black

data = pandas.read_csv(central_park_file)
data1 = data["Primary Fur Color"].value_counts()
data_csv = pandas.DataFrame(data1).to_csv("AngelYu/day25/squirrel_count.csv")
# data_grey = data[data["Primary Fur Color"] == "Gray"]  # Get data with gray fur
#test_count = pandas.Series(data_grey)
# data_count = data_grey.count()  # Get the number of gray squirrels in the data
# print(data_count)


