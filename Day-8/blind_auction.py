from replit import clear
# install replit using pip or pip3 in linux
logo='''

< secret auction >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
'''
print(logo)
print("Welcome to the secret auction program.")
participants={}
while(True):
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    yn=input("Are there any other bidders? Type 'yes' or 'no'\n")
    participants[name]=bid
    if yn=="yes":
        clear()
    else:
        break

max_bidder=""
max_bid=0
for i in participants:
    if(participants[i]>max_bid):
        max_bid=participants[i]
        max_bidder=i
print(f"{max_bidder} wins")


