year=int(input("Enter the Year you want to check is a leap year or not "))
if year%100==0:
    if year%400==0:
        print(year,"is a Centenary Leap Year")
    else:
        print(year,"is not a Centenary Leap Year")
else:
    if year%4==0:
        print(year,"is a Leap Year")
    else:
        print(year,"is not a Leap Year")

