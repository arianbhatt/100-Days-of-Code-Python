Menu={
        "espresso":{
            "ingredients":{
                "water":50,
                "milk":0,
                "coffee":18,
                },
            "cost":1.5,
            },
        "latte":{
            "ingredients":{
                "water":200,
                "milk":150,
                "coffee":24,
                },
            "cost":2.5,
            },
        "cappuccino":{
            "ingredients":{
                "water":250,
                "milk":100,
                "coffee":24,
                },
            "cost":3.0,
            },
        }
money=0.0
resources={
        "water":300,
        "milk":200,
        "coffee":100,
        }
def available(var):
    a=1
    resources_data_backup=resources
    for i in resources:
        if(Menu[var]["ingredients"][i]>=resources[i]):
                a=0
    if a==0:
        print("Sorry We are out of Ingredients")
        return False
    else:
        for i in resources:
            resources[i]=resources[i]-Menu[var]["ingredients"][i]
    return True

while(True):
    cost=0.0
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        print("Thank You for Your Visit ")
        break
    elif choice=="report":
        print(f'Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g \nMoney: ${money}')
        continue
    elif choice=="espresso":
        if(available(choice)):
            cost=Menu["espresso"]["cost"]
        else:
            continue
    elif choice=="latte":
        if(available(choice)):
            cost=Menu["latte"]["cost"]
        else:
            continue
    elif choice=="cappuccino":
        if(available(choice)):
            cost=Menu["cappuccino"]["cost"]
        else:
            continue
    else:
        print("Choose Properly")
        continue
    print(f"Cost of {choice} is ${cost}")
    back=0-(cost)
    submitted=0.0
    while(back<0.0):
        pennies=float(input("How many pennies: "))
        nickles=float(input("How many nickles: "))
        dimes=float(input("How many dimes: "))
        quaters=float(input("How many quaters: "))
        submitted=submitted+(pennies*0.01)+(nickles*0.05)+(dimes*0.1)+(quaters*0.25)
        back=round(submitted-cost,2)
        if(back>=0):
            break
        else:
            print(f"Not Enough Money\nTry A Few More")
    money=money+cost
    print(f"Here is You {choice} Enjoy, Here is the return ${back}")

