print('Hello, welcome to trivia!')

ans = input('Are you ready to play (yes/no): ')

score = 0
total_q = 5
if ans.lower()=='yes':
 ans = input('1. What is the best programming language? ')
 if ans.lower()== 'python':
    score +=1
    print('Correct')
 else:
     print('Incorrect')

ans =input('2. what is 2 + 8 + 9 -1 ?')
if ans == '18':
    score +=1
    print('Correct')
else:
    print('Incorrect')

ans = input('3. What is better a 1050ti or a 1060(graphics card)?')
if ans.lower()=='1060':
    score +=1
    print('Correct')
else:
    print('Incorrect')


ans = input('4.What is the capital city of south sudan ?')
if ans.lower()== 'juba' or ans.lower()== 'khartuom':
    score +=1
    print('Correct')
else:
    print('Incorrect')

ans = input('5.what is the lagest planet ?')
if ans.lower()=='jupiter':
    score+=1
    print('Correct')
else:
    print('Incorrect')



print('Thank you for playing , you got ',score,"Question correct.")
mark = (score/total_q)*100
print("Mark:",str(mark) + '%')
print('Goodbye')





import random

number = random.randint(1,10)
tries = 2

uname = input("Hello, what is your username?")
print("Hello",uname + ".",)

Question = input("Would you like to play a game? [Y/N]")
if Question == "n":
   print("oh..okay")
if Question == "y":
    print("I,m thinking of a number between 1 & 10")
    guess = int(input("Have a guess:"))
    if guess > number:
     print("Guess Lower...")
     if guess < number:
         print("Guess Higher...")
     while guess != number:
         tries +=1
         guess = int(input("Try again: "))
         if guess < number:
            print("Guess Higher")
     if guess == number:
         print("You're right! you win! The number was",number,\
                   "and it only",tries, "tries!")



