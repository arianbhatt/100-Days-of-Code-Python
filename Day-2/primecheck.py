number=int(input("Enter the number that you want to check "))
c=0
for i in range(2,number//2):
    # the % operator returns the remainder 
    if(number%i==0):
        c+=1
if(c==0):
    print(number," is a Prime Number")
else:
    print(number," is not a Prime Number")

