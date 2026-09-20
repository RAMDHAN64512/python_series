# #taking input from the user

# name=input("Enter your name ")
# print(name) #string input

# print(type(name))

# #integer as input
# print("Are you 18+ person 'True' or 'False'")
# b=int(input("Enter your age "))
# print("your age is",b)
# print(type(b)) #int as input

# if b<18:
#     print("you are minor now")
# else:
#     print("You are mature person now")    



#taking boolean as input
# print("Give your answer as True or False")
# abc= input("You study daily ")
# is_true = abc.lower()==True
# print(is_true)
# print(type(is_true))

# if is_true==True:
#     print("You are genius person")
    
# else :
#     print("You are lazy person")    

# implementation of lower() function
# name=input("Enter your name ")
# abc=name.lower()
# print(abc)


#tuple as input

value = input("Enter integer values ")
my_tuple = tuple(map(int,value.split()))
print(my_tuple)
print(type(my_tuple))
