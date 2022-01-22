print("Welcome to the rollercoaster!")
height=int(input("What is your Height? "))
if height >= 120:
    print("You can ride the Rollercoaster")
    age= int(input("What is your age "))
    bill=0
    if age<=12:
        bill=5
        print("Please Pay $5")
    elif age<=18:
        bill=7
        print("Please Pay $7")
    else:
        bill=12
        print("Please Pay $12")
    photo=input("Do you want a photo taken? Y or N. ")
    if photo=='Y':
        bill+=3
    print("Your Final bill is $",bill)
else:
    print("Sorry, you have to grow taller before you can ride.")
