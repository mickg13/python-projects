num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))





country_profile ={
   'country:south sudan','capital city:"Juba', 'Offcial languages : English & Swahili','popultion :12,778,250',
}


print(country_profile)                                  




import logging

# create and configure logger
logging.basicConfig(filename="E:\\python\\lumberjack.log")
logging = logging.getLogger()

import sys

def gen(n):
   for i in range(n):
      yield i ** 2


g = gen(10000)

for i in g:
   print(i)

























