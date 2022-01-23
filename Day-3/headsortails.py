import random
# getting seed
s=int(input("Create a seed number for toin flip: "))
random.seed(s)
# will create a random floatinf point from 0 to 1.99999
test=int(random.random()*2)
if(test==1):
    print("Heads")
else:
    print("Tails")

