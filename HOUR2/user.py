username="rudra"
password=543321

user=input("Username dalo Bhai! ")
small=user.lower()
gpass=int(input("PIN dalo Bhai! "))

if small==username and gpass==password:
    print("Welcome to the system")

else:
    print("Username or PIN is incorrect")
    