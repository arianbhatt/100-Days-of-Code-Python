# taking height and weight
height=float(input("Enter your height in m: "))
weight= float(input("Enter your weight in kg: "))
# calculating BMI using formula
BMI=weight/height**2
print("Your BMI is: \n",int(BMI))
# the above int() will convert BMI which was float to integer basically removes everything after decimal
