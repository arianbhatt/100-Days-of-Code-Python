height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))
BMI=round(weight/height**2)
if BMI<18.5:
    print("Your BMI is ",BMI," You are Underweight")
elif BMI>18.5 and BMI<=25:
    print("Your BMI is ",BMI," You have Normal Weight")
elif BMI>25 and BMI<=30:
    print("Your BMI is ",BMI," You are Overweight")
elif BMI>30 and BMI<=35:
    print("Your BMI is ",BMI," You are Obese")
else:
    print("Your BMI is ",BMI," You are Clinically Obese")

