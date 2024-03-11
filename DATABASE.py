'''
QUESTION 1: As a senior backend engineer at company, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:

1). Insert the profile information for a new user.
2). Find the profile information of a user, given their username
3). Update the profile information of a user, given their usrname
4). List all the users of the platform, sorted by username
You can assume that usernames are unique.
'''


class user:
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email
    def __repr__(self):
        return "USER(username = {}, name = {}, email = {})".format(self.username,self.name,self.email)
    def __str__(self):
        return self.__repr__()

rithin = user('ritu','rithin','rithin00201@gmailcom')
aakash = user('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = user('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = user('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = user('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = user('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = user('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = user('vishal', 'Vishal Goel', 'vishal@example.com')

users = [rithin,aakash,biraj,hemanth,jadhesh,siddhant,sonaksh,vishal]


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user = database.find('siddhant')
print(user)


database.insert(rithin)

print(database.list_all(),'\n')

