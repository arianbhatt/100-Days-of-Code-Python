# number divisible by 3 fizz
# number divisible by 5 buzz
# number divisible by both fizzbuzz

for i in range(1,101):
    if(i%3==0 and i%5!=0):
        print("Fizz")
    elif(i%5==0 and i%3!=0):
        print("Buzz")
    elif(i%5==0 and i%3==0):
        print("FizzBuzz")
    else:
        print(i)

