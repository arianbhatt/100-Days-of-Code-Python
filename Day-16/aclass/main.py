class User:
    # Constructer Part of the Blueprint that allows us to specify what should happen when our object is being constructed.
    def __init__(self, user_id, username):
        #initialise attributes
        print("new user is being created")
        self.id=user_id
        # we can have the name of self.id as self.user_id too
        self.username=username
        # we can create attributes with some default values.
        self.school="A Nice School Name"
    def change_username(self,user):
        user.username=input("Enter the new Username ")



# Every object we create now needs 2 attributes an id and a username
user_1 = User("001","Aryan")
print(user_1.id," ",user_1.username)
print(user_1.school)
user_1.change_username(user_1)
print(user_1.id," ",user_1.username)

