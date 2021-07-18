
import math

mark1 = int(input("please Enter grade 1:"))
mark2 = int(input("please Enter grade 2:"))
mark3 = int(input("please Enter grade 3:"))
mark4 = int(input("please Enter grade 4:"))
mark5 = int(input("please Enter grade 5:"))

total_avergae = ((mark1+mark2+mark3+mark4+mark5)/5)
print("total avergae is",total_avergae)




import datetime

goanar_birth = datetime.date(1995,11,24)
print("goanar_birth",goanar_birth)

print(goanar_birth.strftime("%A,%B %d,%Y"))
message = "goanar_birth was on {:%A,%B %d,%Y}."

print(message.format(goanar_birth))

today = datetime.date.today()
print("Toady",today)






import datetime
year = int(input("please enter the year you were born"))
month = int(input("please enter the month you were born "))
day = int(input("please enter the day you were born"))

DOB = datetime.datetime(year,month,day)
Age = (datetime.datetime.now()-DOB)
print("you are " + str(Age.days)+ "days old")

convertdays = int(Age.days)
AgeYear = convertdays/365

print("or "+ str(AgeYear)+  " year old to be less precise!")




import random

def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step =random.choice(['N','S','E','W'])
        if step == 'N':
            y = y +1
        elif step == 'S':
            x = x+1
        elif step == 'E':
            x = x+1
        else:
            x= x-1
        return (x,y)
for i in range(25):
    walk = random_walk(10)
    print(walk,"Distance from home = ",abs(walk[0])+abs(walk[1]))





import random

for i in range(1000):
    print(random.random())




planets =[
    ("Mercury",2440,5.43,0.395),
    ("Venus",6052,5.24,0.723),
    ("Earth",6378,5.52,1.000),
    ("Mars",3396,3.93,1.530),
    ("Jupiter",71492,1.33,5210),
    ("Saturn",60268,0.69,9.551),
    ("Uranus",25559,1.27,19.213),
    ("Neptune",24764,1.64,30.070)
    ]
size = lambda planets: planets[1]
planets.sort(key=size,reverse=True)
print(planets)





