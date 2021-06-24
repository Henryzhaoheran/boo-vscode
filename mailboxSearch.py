# Get user's mailbox information. 
'''
    1. user's mailbox list: hello@domain.com;test@hotmail.com;bob@domain.com;jerry@hotmail.com;lee@live.com
    2. When user input domain name, the program returns user name list.

'''

# The source user email list data
data = 'hello@domain.com;test@hotmail.com;bob@domain.com;jerry@hotmail.com;lee@live.com'

#initialize an empty dictionary to store email user and email domain information.
users = {}

#split user's mailbox and save it into a list. 
datalist = data.split(";")

'''
# Idea 1

# add each mailbox to a dictionary 
for mbox in datalist:
    #split each email address by @ to get user name and domain name
    mboxlist = mbox.split("@")
    #save the user name and domain name into the users dictionary.
    # user name is the kay, domain is value
    users[mboxlist[0]] = mboxlist[1]

print(users)

# user input informaiton to search domain.
user_input_search=input("Please input the mailbox domain you would like to search: ")

for name, domain in users.items():
    if domain == user_input_search:
        print(name)
'''

# idea 2
# add each mailbox to the dictionary

for mbox in datalist:
    #split each email address by @ to get user name and domain name
    mboxlist = mbox.split("@")
    mail_domain = mboxlist[1]
    mail_user = mboxlist[0]
    #save the user name and domain name into the users dictionary.
    if mail_domain in users:
        #if domain is in the dict, add the users to key (key is a list)
        user_list = users[mail_domain] 
        user_list.append(mail_user)
        #print(user_list)
        users[mail_domain] = user_list
        #print(users)
    else:
        #if domain is not in the dict, add the user to an empty list. 
        #print(mail_user)
        #print(type(mail_user))
        user_list=[]
        user_list.append(mail_user)
        #print(user_list)
        users[mail_domain] = user_list
        #print(users)

print(users)

# https://www.bilibili.com/video/BV1mB4y1F74v?p=38





