from game_data import data
from art import logo, vs
import random
from replit import clear

def format_data(account):
    """To format that dictionary and return a nice arranged string (f-string btw."""
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
def check_answer(guess,a_followers,b_followers):
    if a_followers>b_followers:
        return guess=='A'
    else:
        return guess=='B'
print(logo)
score=0
cont=True
account_b=random.choice(data)
while(cont):
    account_a=account_b # dictionary from list data
    account_b=random.choice(data)
    if (account_a==account_b):
        account_b=random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")
    # asking for a guess
    guess=input("Who has more Instagram Followers 'A' or 'B': ")
    is_correct=check_answer(guess,account_a['follower_count'],account_b['follower_count'])
    clear()
    print(logo)
    if is_correct:
        score+=1
        print(f"You are right! current score is {score}.")
    else:
        cont=False
        print(f"Sorry that is wrong. Final Score is {score}.")







