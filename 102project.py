"""I dont like to to calculations of maths so i am building this calculator"""

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("Enter 1 for add")
print("Enter 2 for substract")
print("Enter 3 for multiply")
print("Enter 4 for divide")
choose = int(input("enter the operation to be performed"))            

def add1(x,y):
    return x+y
def substract1(x,y):
    return x-y
def multiply1(x,y):
    return x*y
def divide1(x,y):
    return x/y

if (choose == 1):
  print(add1(num1,num2))
elif (choose == 2):
  print(substract1(num1,num2))  
elif (choose == 3):
  print(multiply1(num1,num2))
elif (choose == 4):
  print(divide1(num1,num2))
else:
    print("Enter a Valid Input")            


