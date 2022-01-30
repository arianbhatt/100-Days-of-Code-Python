import random

user_cards=[random.randint(1,10),random.randint(1,10)]
dealer_cards=[random.randint(1,10)]
user_score=sum(user_cards)
print(f"Your cards:{user_cards}, current score: {user_score}")
print(f"Computer's first card:{dealer_cards[0]}")
dealer_score=sum(dealer_cards)
for i in user_cards:
    if( i == 1):
        choice=input("You have a Ace in your Cards what do you want your ace to count as: Type '1' for 1 '11' as 11 ")
        if(choice =='11'):
            user_cards[user_cards.index(1)]=11
while (True):
    yn=input("Type 'y' to get another card, type 'n' to pass: ")
    dealer_cards.append(random.randint(1,10))
    if(yn=='y'):
        user_cards.append(random.randint(1,10))
        for i in user_cards:
            if( i == 1):
                choice=input("You have a Ace in your Cards what do you want your ace to count as: Type '1' for 1 '11' as 11 ")
                if(choice =='11'):
                    user_cards[user_cards.index(1)]=11
        
    else:
        user_score=sum(user_cards)
        if(sum(dealer_cards)<17):
            c=0
            for i in dealer_cards:
                if (i==1):
                    user_cards[c]=11
                c+=1
            if(sum(dealer_cards)<17):
                    dealer_cards.append(random.randint(1,10))
               
        dealer_score=sum(dealer_cards)
        print(f"Your final hand :{user_cards}, final score{user_score}")
        print(f"Computer's final hand :{dealer_cards}, final score{dealer_score}")
        if(user_score>21):
            print("You went Over :( ")
        elif(user_score>dealer_score):
            print("You won :) ")
        elif(user_score==dealer_score):
            print("Its Draw :/ ")
        elif(dealer_score>21):
            print("The Computer went over You get back what you bet")
        elif(dealer_score>user_score):
            print("Computer won :)")
        else:
            print("A Situation I don't know who won occured ")
        break
