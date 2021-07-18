def get_formatted_name(first,last):
    """Gererate a neatly formatted full name"""
    full_name = first + ' ' + last
    return full_name.title()

from name_function import get_formatted_name
print("Enter 'q' at any time to quit . ")
while True:
    first = input("\n plaese give me a first name: ")
    if first == 'q':
        break
    last = input("plases give me a last name : ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print("\ neatly formatted name : " + formatted_name + '.')



import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""
    def tset_first_last_name(self):
        """Do names like john , james work ?"""
        formatted_name = get_formatted_name('john','james')
        self.assertEqual(formatted_name,'john james')


unittest.main()


#function
def describe_pet(animal_typy,pet_name):
    """Display information about a pet ."""

    print("\nI have a " + animal_typy + ".")
    print("my " + animal_typy + "'s name is " + pet_name.title() +".")
describe_pet('dog' ,'mindy')



def display_message(message_type,sendr_name):
    """Display message to resiver !"""
    print("\n Hello good afternoon! " + message_type + ".")
    print("I am " + sendr_name.title() )
display_message('hey','Goanar')




def greet_uesrs(names):
    """print a simple grrting to each uesr  in the list . """
    for name in names:
        message = "Hello " + name.title() + "!"
        print(message)


uesrnames = ['Goanar','Gatkoth','Taban',]
greet_uesrs(uesrnames)





