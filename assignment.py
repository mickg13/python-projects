USERS = [
    {
        "username": "Androuk",
        "password": "NeverGonnaGiveYouUp",
        "email": "androuk@gmail.com",
        "messages": []
    },
    {
        "username": "Mubarak",
        "password": "NeverGonnaLetYouDown",
        "email": "mubarak@gmail.com",
        "messages": []
    },
    {
        "username": "Meseret",
        "password": "NeverGonnaRunAround",
        "email": "meseret@gmail.com",
        "messages": []
    },
    {
        "username": "KingG",
        "password": "AndDesertYou",
        "email": "kingg@gmail.com",
        "messages": []
    },
    {
        "username": "Abrham",
        "password": "NeverGonnaMakeYouCry",
        "email": "abrham@gmail.com",
        "messages": []
    },
    {
        "username": "Adda",
        "password": "NeverGonnaSayGoodbye",
        "email": "adda@gmail.com",
        "messages": []
    },
    {
        "username": "Philmon",
        "password": "NeverGonnaTellALie",
        "email": "philmon@gmail.com",
        "messages": []
    },
    {
        "username": "Efrem",
        "password": "AndHurtYou",
        "email": "efrem@gmail.com",
        "messages": []
    },
]


def get_email(username, password):
  for user in USERS:
      if user['username'] == username:
       if user['password'] == password: #case (iii)
        return user['email']
       else:
        print('Incorrect password') #case (ii)
        return None
  print(f'No such user {username}') #case (i)
  return None

get_email("Philmon", "AndHurtYou")
get_email("Efrem", "AndHurtYou")
get_email("Efremm", "swordfish")
get_email("Philmon", "NeverGonnaTellALie")
get_email("Efrem", "AndHurtYou")
get_email("Efrem", "AndHurtYou") 





def create_message(sender, receiver, text):
  message = {'to': receiver,'from': sender,'text': text}
  sender_email = 0
  receiver_email = 0
  for user in USERS:
    if user['email'] == sender:
      sender_email = 1
    elif user['email'] == receiver:
      receiver_email = 1
    if receiver_email == 1 and sender_email == 1:
     return message
  else:
     if sender_email == 0:
      print(f'Email {sender} doesn\'t exist')
     if receiver_email == 0:
       print(f'Email {receiver} doesn\'t exist')
     return None

create_message ("efrem@gmail.com","philmon@gmail.com","yo")
create_message ("efrem@gmail.com","philmon@gmail.com","yo")
create_message ("efrem@gmail.com","phillmon@gmai.com","yo")
create_message ("efremm@gmail.com","phillmon@gmail.com","yo")





def get_username_by_email(username,password,recipient,text):
  sender_email = get_email(username, password) #question 1
  if sender_email: #checks to see if it is not None
    message = create_message(sender_email, recipient, text) #question 2
    for user in USERS:
      if user['email'] == recipient or user['email'] == sender_email:
        user['messages'].append(message)


get_username_by_email("Phillmon","swordfish","XXX@gmail.com","Yo")
get_username_by_email("Philmon","swordfish","XXX@gmail.com","Yo")
get_username_by_email("Philmon","NeverGonnaTellALie","XXX@gmail.com","Yo")
get_username_by_email("Philmon","NeverGonnaTellALie","efrem@gmail.com","Yo")




#Exception

try:
    print("hello world.")
except:
    print("something went wrong when writing to the file")
else:
   print("Nothing went wrong")


class Rational:
    def __init__(self, numer, denom=1):
        if not isinstance(numer, int):
            print(f"Raising a Type error... numer is {type(numer)}")
            raise TypeError(f"Numerator '{numer}' must be an integer!")
        if not isinstance(denom, int):
            raise TypeError(f"Denominator '{denom}' must be an integer!")
        if denom == 0:
            raise ZeroDivisionError(f"Denominator of a rational cannot be zero")

        self.numer = numer
        self.denom = denom

    def __repr__(self):
        return f"{self.numer}/{self.denom}"

    def decimal(self):
        return self.numer / self.denom

    def __mul__(self, other):

        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(self.numer * other.numer,
                        self.denom * other.denom)

    # Homework
    def __truediv__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(self.numer * other.denom,
                        self.denom * other.numer)

    def __add__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(self.numer * other.denom + self.denom * other.numer,
                        self.denom * other.denom)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(self.numer * other.denom - self.denom * other.numer, other.denom * self.denom)


x = Rational(1, 2)
y = 4

a = x * y
b = x / y

print(a)
print(b)

x = Rational(1, 2)
y = 4

a = x + y
print(a)

x = Rational(1, 2)
y = 5

b = x - y
print(b)










