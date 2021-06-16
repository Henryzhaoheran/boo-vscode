'''
user login, 
3 chances to input
success -------> login success
fail --------> how many chances left
chances used out, --------> login failed
'''

db_user="bob"
db_pwd="pwd"



chances = 3
'''
if input_user == db_user:
    if input_pwd == db_pwd:
        print("Login successful")
elif chances > 0:
    chances = chances - 1
    print("Login failed, %i times left, please input"%chances)
else:
    print("Login failed, please exit")
'''

while chances > 0:
    input_user=input("User Name: ")
    input_pwd=input("Password: ")
    chances = chances - 1
    if input_user == db_user and input_pwd == db_pwd:
        print("="*30)
        print("Login successful")
        #chances = 0
        break
    elif chances >= 1:
        print("Login failed, %i times left, please input"%chances)
    else:
        print("Login failed, please exit")
