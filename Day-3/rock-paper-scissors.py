import random
# Rock Paper Scissors Game
# github: arianbhatt
print("Rules:\n*Rock wins agains Scissors\n*Scissors wins against paper\n*Paper wins against rock.")
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

signs=[rock,paper,scissors]
if(choice >2):
    print("Are You Stupid. You Lose.")
else:
    computer=random.randint(0,2)
    print(f"You Chose\n{signs[choice]}")
    print(f"The Computer Chose\n{signs[computer]}")
    if(choice==computer):
        print("It's a Draw")
    elif((choice==0 and computer==2) or (choice==1 and computer==0) or (choice==3 and computer==1)):
        print("You Won :)")
    else:
        print("The Computer Won :(")
