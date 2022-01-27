def prime_check(num):
    count=0
    for i in range(2,num):
        if(num%i==0):
            count+=1
            break
    if count==0:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
number=int(input("Enter the Number you want to check is Prime or Not "))
prime_check(number)

