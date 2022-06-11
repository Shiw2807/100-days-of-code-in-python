# # with open ("weather.csv", mode="r") as file:
# #     print(file.readlines())
  

# # import csv

# # with open("weather.csv") as data_file:
# #     data=csv.reader(data_file)
# #     temperatures=[]
# #     for row in data:
# #         print(row)
# #         if(row[1]!="temp"):
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# import pandas as pd

# data=pd.read_csv("weather.csv")


# temp_list=data["temp"].to_list()
# # # l=len(temp_list)
# # # avg=sum(temp_list)/l
# # # print(avg)

# # print(data[data["day"] == "Monday"])
# # print(data[data["temp"] == max(temp_list)])

# monday= data[data["day"] == "Monday"]
# print(f"{int(monday.temp)* 1.8 +32} F")

import pandas as pd

data=pd.read_csv("Squirrel.csv")

Gray=len(data[data["Primary Fur Color"]=="Gray"])
Cinnamon=len(data[data["Primary Fur Color"]=="Cinnamon"])
Black=len(data[data["Primary Fur Color"]=="Black"])

data_dict={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count":[Gray,Cinnamon,Black]
}

df=pd.DataFrame.from_dict(data_dict)
df.to_csv("Squirrel Count.csv")





