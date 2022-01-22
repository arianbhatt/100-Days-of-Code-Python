# .lower() changes uppercase to lowercase
# .count() counts the number ot times a character occurs in our string
print("Welcome to the love Calculator!")
name1=input("What is your name? \n")
name2=input("What is their name? \n")
name_combined=name1.lower()+name2.lower()
a=0
b=0
for i in 'true':
    c=name_combined.count(i)
    a=a+c
for i in 'love':
    c=name_combined.count(i)
    b=b+c
percent=a*10+b
if percent>100:
    s=0
    while percent>0:
        d=percent%10
        s=s+d
        percent=percent//10
    percent=s
if(percent<=10 and percent>=90):
    print("Your score is",percent,"You go together like coke and mentos")
elif(percent>=40 and percent<=50):
    print("Your score is",percent,"You go alright together")
else:
    print("Your score is",percent)



