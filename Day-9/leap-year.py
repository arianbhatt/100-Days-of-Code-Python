def is_leap(ycheck):
    """This funciton takes an integer in this case a year and returns if that year is leap year or not True or False"""
    if ycheck%100==0:
        if ycheck%400==0:
            return True
        else:
            return False
    else:
        if ycheck%4==0:
            return True
        else:
            return False
def days_in_month(yr,mn):
    """This function takes in the year and month and returns the number of days in that month"""
    if mn>12 or mn<1:
        return "Invalid Month"
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(is_leap(yr) and mn==2):
        return 29
    else:
        return month_days[mn-1]
year=int(input("Enter a year: "))
month=int(input("Enter a month: "))
days=days_in_month(year,month)
print(days)
        


