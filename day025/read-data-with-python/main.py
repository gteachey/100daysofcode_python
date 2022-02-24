import csv
import pandas
import math

# with open("weather_data.csv") as weather_file:
#    data = weather_file.readlines()
#   print(data)
#
# #with open("weather_data.csv") as weather_file:
# #    data = csv.reader(weather_file)
# #    temperatures = []
# #    for row in data:
# #        print(row)
# #        if row[1] != "temp":
# #            temperatures.append(int(row[1]))
# #
# #    print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
# #print(data)
# #print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# #
# # data["temp"].mean()
# # max_temp = data["temp"].max()
# #
# # print(data[data.temp == max_temp])
# #
# # monday = data[data.day == "Monday"]
# # # Temperature in celsius degree
# # celsius = int(monday.temp)
# #
# # # Converting the temperature to
# # # fehrenheit using the above
# # # mentioned formula
# # fahrenheit = (celsius * 1.8) + 32
# #
# # print("{}".format(fahrenheit))
#
# # Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "Tom"],
#     "scores": ["32", "53"]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

print(black_squirrel_count)
color_total = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [black_squirrel_count, red_squirrel_count, gray_squirrel_count]
}
# for color in data["Primary Fur Color"]:
#     if color == "Cinnamon":
#         color_total['Count'][1] += 1
#     elif color == "Gray":
#         color_total['Count'][0] += 1
#     elif color == "Black":
#         color_total['Count'][2] += 1
#     else:
#         color_total['Count'][3] += 1

print(color_total)
to_csv = pandas.DataFrame(color_total)
to_csv.to_csv("squirrel_count.csv")
