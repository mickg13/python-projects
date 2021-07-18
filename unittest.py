#import unittest


#class MyTestCase(unittest.TestCase):
   # def test_something(self):
       # self.assertEqual(True, False)


#if __name__ == '__main__':
    #unittest.main()




def tupleFromString(s):
    #converts a string like `(3,7)` to the correspoding int tuple
    s = s.strip()
    arguments = s[1:len(s)-1].split(',')
    return tuple(int(i) for i in arguments)


print(tupleFromString('(3,5)'))


import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def gen(n):
    for i in range(n):
        yield i ** 2


g = gen(10000)
for i in g:
    print(i)

