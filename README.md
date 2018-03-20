with open('pi_digits.txt') as file_project:
    contents = file_project.read()
    print(contents)


error:
1 ZeroDivisionError
2 try-except
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist!"
    print(msg)



import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What's your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print("We'll remember you when you come back, " + username + " !")
else:
    print("Welcome back! " + username + " !")
    
    
