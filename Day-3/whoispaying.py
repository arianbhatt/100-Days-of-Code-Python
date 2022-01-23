import random
num=int(input("Create a Seed: "))
namesAsCSV=input("Give me everybody's names, seperated by commas ")
names=namesAsCSV.split(", ")
l=len(names)
index=random.randint(0,l-1)
print(names[index],"will pay :) ")
