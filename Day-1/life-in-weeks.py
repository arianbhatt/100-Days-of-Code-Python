# this program calculates the number of weeks days and months left till the age of 90 form your current age
age=int(input("How old are you? "))
years_left=90-age
days_remaining=years_left*365
weeks_remaining=years_left*52
# this program assumes that a year has 365 days and 52 weeks and also that you will live upto 90 years of age 
print(f"You have {days_remaining} days, {weeks_remaining} weeks, {years_left} years")

