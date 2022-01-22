print("Welcome to Italiano Pizza Deliveries!")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")
size=input("What size pizza do you want? S,M,L ")
bill=0
if size=='S':
    bill=15
elif size=='M':
    bill=20
else:
    bill=25

if size=='S':
    add_pepperoni=input("Add Pepperoni for +$2 Y/N ")
    if add_pepperoni=='Y':
        bill+=2
else:
    add_pepperoni=input("Add Pepperoni for +$3 Y/N ")
    if add_pepperoni=='Y':
        bill+=3
add_cheese=input("Add Extra Cheese for +$1 Y/N ")
if add_cheese=='Y':
    bill+=1
print("You Final Bill is",bill)
