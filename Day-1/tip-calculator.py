# printing the welcome prompt
print("Welcome to the tip calculator.")
# asking for the bill
bill=float(input("What was the Total Bill? "))
# asking for tip percentage
percent=float(input("What percentage of the bill would you like to give? 10, 12, 15? "))
# getting the number of people
people=int(input("How many people to split the bill? "))
tip=(bill*percent)/100
per_head=(bill+tip)/people
# rounding of the bill to 2 decimal places
final=round(per_head,2)
print('Each Person should pay: ',final )


