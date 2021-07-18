cares = ['audi','bmw','subaru','tayota']
for car in cares:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())




age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet ?")
else:
    print("you are too young to vote!")
    print("please register to vote as soon as you trun 18!")

age = 19
if age >= 18:
    print("you are too old enough to vote !")
    print("have you registered to vote yet ?")



"Admissoion for anyone under age 4 is free "
"Admission for anyone between the age of 4 and 18 is $5"
"Admission for anyone age 18 or under is $10 ."


age = 12
if age < 4:
    print("your adission cost is $0 .")
elif age < 18 :
    print("your admission cost is $5 .")
else:
    print("your admission cost is $10 .")




# second way


age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 5
else :
    price = 10
print("your admission cost is $" + str(price)+ ".")




# Testing multible condioins


requested_toppings = ['tuna ','mushroomes', 'extra cheese','black olives','pepperoni']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")






avalable_toppings = ['onino','black''susage','green peppers','pepperoni','pinapple']

requested_toppings = ['tuna ','mushroomes', 'extra cheese','black olives','pepperoni']

for requested_topping in requested_toppings :
    if requested_topping in avalable_toppings:
        print("Adding " + requested_topping + ".")
    else:
     print("sorry we don,t have " + requested_topping + ".")

print("\n Finised making you pizza!")





