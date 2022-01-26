import random
import letter_guess
from hangman_word import word_list
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
random_word=random.choice(word_list)
print("Trial it is ",random_word)
list_check=[]
lives=6
for i in range(len(random_word)):
    list_check.append("_")
while(True):
    st=""
    user=input("Guess a letter ").lower()
    lives,list_check=letter_guess.check(user,random_word,list_check,lives)
    for i in list_check:
        st=st+i+" "
    print(st)
    if(lives==0):
        print("You Lose!!!")
        break
    if("_" not in list_check):
        print("You Won!!! Yeahhh")
        break

