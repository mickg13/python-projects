my_list = [0,1,2,3,4,5,6,7,8,9]
# 0,1,2,3,4,5,6,7,8,9
# -10,-9,-8,-7,-6,-5,-4,-3,-2,-1



# list[start:end:stop]



print (my_list)






names = ['Peter Parker','Clark Kent','Wade Wilson','Bruce Wayne']
heroes = ['Spiderman ','Superman','Deadpool','Batman']
universes = ['Marvel','DC','Marvel','DC']

for name,hero,universe in zip(names,heroes,universes):
    print(f'{name} is actually {hero} from {universe}')




# HOW TO WRITE A DICTIONARIES TO CSV FILE AND READ WITH PYTHON


import csv



def write_csv(data):
    with open ('persons.csv','a')as file:
        writer = csv.writer(file)

        writer.writerow([data['surname'],data['name'],data['age']])


def write_csv2(data):
    with open ('persons.csv','a')as file:
        order = ['surname','name','age']
        writer = csv.DictWriter(file,fieldnames=order)
        writer.writerow(data)

def read_csv():
    with open('persons.csv')as file:
        keys = ['name','surname','age']
        reader = csv.DictReader(file,fieldnames=keys)

        results = []

        for row in reader:
            results.append(dict(row))
        return results







def main ():
    d = {'surname':'Thomas','name':'Dut','age':78}
    d1 = {'surname':'Abraham','name':'Bol','age':70}
    d2 = {'surname':'Goanar','name':'Abraham','age':24}
    d3 = {'surname':'Peter','name':'Adalino','age':25}
    d4 = {'surname':'Machar','name':'Abraham','age':26}

    c = [d,d1,d2,d3,d4]
    for item in c:
        write_csv(item)

if __name__ == '__main__':
    main()


rows = read_csv()
print(rows)








