# user_choice is the user choice
# choosen is the randomly generated word
# array is the array that keeps the guessed and remaining
# count hold the number of lives

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def check(user_choice_var,choosen,array,count):
    if user_choice_var not in choosen:
        count-=1
        print(f"You guessed {user_choice_var} , that's not in the word You Lose a Life {count} lives left ")
    if user_choice_var in array:
        print("The Letter is already choosen ")
    for i in range(0,len(choosen)):
        if(choosen[i]==user_choice_var):
            array[i]=user_choice_var
    print(stages[count])
    return count,array

