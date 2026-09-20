print("Enter three numbers , to know who is gretest")

a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
#23 12 25
if a>b and a>c:
    print("A greater")  #23>12
    
elif b>a and b>c:
    print("B is greater")
    
elif c>a and c>b :
    print("C greater")  
    
print("your total score is ",a+b+c)