shopping_basket ={}

print("""
shopping basket Options
------------------------
1: Add item 
2: Remove item
3: View item
0: Exit program 

""")



option = int(input("Enter an option: "))

while option !=0:
    if option ==1:
        item = (input("Enter an item: "))
        if item in shopping_basket:
            print("Item already in shopping basket")
            qnty = int(input("Enter the quantity: "))
            shopping_basket[item] = shopping_basket[item]+qnty
        else:
            qnty = int(input("Enter the quantity: "))
            shopping_basket[item] = qnty

    elif option ==2:
        item = input("Enter an item: ")
        del (shopping_basket[item])

    elif option == 3:
        for item in shopping_basket:
            print(item,":",shopping_basket[item])


    elif option !=0:
        print("you did,t enter a valid number.")
    option = int(input("\n\nEnter an option:"))
else:
    print("shopping basket program closed.")










#password
from random import *
num = "0123456789"
alphanum = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFIGHIJKLMNOPQRSTUVWXYZ"
spalphanum= "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'#@+(){}"
passlen = int(input("Enter password length \n"))
randpass= []
print("Select the type of passwords \n1. Numbers \n2. Alphanum\n3.Special alphanumeric\n")
Selecttype = int(input())

if Selecttype == 1:
  for i in range (passlen):
      randpass.append(choice (num))
elif Selecttype == 2:
  for i in range (passlen):
      randpass.append(choice(spalphanum))

result = "". join(randpass)
print("your random password is :"+result)


#buiding a calcilater

def add(a,b):
    reslut=a+b
    print("a+b= ",result)


def sub(a,b):
    reslut=a-b
    print("a-b= ",reslut)


def mul(a,b):
    reslut=a*b
    print("a*b= ",reslut)

def div(a,b):
    reslut=a/b
    print("a/b= ",reslut)

a= int(input("Enter the first number: "))
b= int(input("Enter the secound number: "))
op= input("Enter the operator: ")


if op== "+":
    add(a,b)
elif op== "-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)

else:
    print("Invalid number: ")

