import pandas
data =pandas.read_csv("Squirrel_Data.csv")
dict_small={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[(data["Primary Fur Color"]=="Gray").count(),
    (data["Primary Fur Color"]=="Cinnamon").count(),
    (data["Primary Fur Color"]=="Black").count()
    ]
}
color_data=pandas.DataFrame(dict_small)
color_data.to_csv("fur_color.csv")
