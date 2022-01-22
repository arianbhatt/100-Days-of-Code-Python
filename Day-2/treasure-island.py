print("Welcome to Treasure Island \nYour Mission is to find the treasure.")
choice1=input("You are at a Crossroad Choose left or right \n")
if choice1=='left':
    choice2=input("You have reached the sea you want to swim or wait for a boat?\n")
    if choice2=='wait':
        choice3=input("You found a Boat.\nYou have reached the island\nYou see three doors in front of you. red blue and yellow. which door will you Enter.\n")
        if choice3=='red':
            print("Ahhhhhhh!!! There is Fire")
            print("Game Over")
        elif choice3=='blue':
            print("Ahhhhhh!!!! You fell into a trap")
            print("Game Over")
        else:
            print("Hurray You found One Piece!!!")
            print("You Won")
    else:
        print("You started swimming")
        print("Ahhhhh! Shark")
        print("A Shark attacked you")
        print("Game Over")
else:
    print("You Found a Jungle")
    print("You are Lost")
    print("Game Over")

