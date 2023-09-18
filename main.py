import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = len(data[data["Primary Fur Color"] == "Black"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(black)
print(gray)
print(cinnamon)

dic = {
    "color" : ["black", "gray", "cinnamon"],
    "count" : [black,gray,cinnamon]
}
df = pd.DataFrame(dic)
df.to_csv("pop_of_s")
