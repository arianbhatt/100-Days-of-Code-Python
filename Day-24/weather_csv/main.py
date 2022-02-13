#with open("weather_data.csv","r") as file:
#   data=file.readlines()
#    print(data)

#import csv
#with open("weather_data.csv") as data_file:
#    data=csv.reader(data_file)
#    temperatures=[]
#    for row in data:
#        if row[1] !="temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas
data =pandas.read_csv("weather_data.csv")
# print(type(data)) pandas dataframe
"""
The 2d Data is Dataframe, the whole table.
The 1d Data is called Series, a row or coloumn
"""
#print(data["temp"])
#data_dict=data.to_dict()
#print(data_dict)

#temp_list=data["temp"].to_list()
# To calculate the avg temperature
#print(sum(temp_list)/len(temp_list))

# pandas way
print(data["temp"].mean())

# To find the maximum Temprature value
print(data["temp"].max())

# Get Data in Coloumn
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

# Get Data for row where temp max
print(data[data.temp==data["temp"].max()])

# Create a dataframe from scratch
data_dict={
    "students":["Sunio","Gian","Nobita"],
    "scores":[76,56,65]
    }
data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
#print(data)
