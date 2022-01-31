import random

logo='''
 -----------------------
< guess the number game >
 -----------------------
        \    ⟋|､
            (°､ ｡ 7
            |､  ~ヽ
            じしf_,)/  
'''
print(logo)
print("I am thinking of a number between 1 and 100.")
num=random.randint(1,100)
choice=input("Choose a difficulty. Type 'easy' or 'hard': ")
lives=0
if choice =='easy':
    lives=10
elif choice =='hard':
    lives=5
def check(user_choice):
    if(user_choice>num):
        print("Go Low")
        return 0
    elif(user_choice<num):
        print("Go High")
        return 0
    else:
        print("Yeah. YOu Guessed the Number")
        return 1

if(lives==0):
    print("Can't even choose difficulty properly :/")
    print("Rerun to play")
else:
    print(f"You have {lives} chances ")
while(lives>0):
    user=int(input("Enter your guess: "))
    a=check(user)
    if(a==1):
        break
    lives-=1
    if lives==0:
        print("Out of Chances")
        break
    print(f"You have {lives} chances ")
    print(f"guess again")
