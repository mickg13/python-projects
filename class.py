class student:
    def __init__(self,fname,age,year):
        self.name = fname
        self.age = age
        self.year = year




class Hello:
    pass
a = Hello()

a.greeting = 'good morning'
print(a.greeting)
b = Hello()
b . greeting = 'My name is Goanar '

print(b.greeting)



class dog:
    def __init__(self,name,birthyaer,color):
        self.name ,self.birthyaer,self.color = name,birthyaer,color
        self.playmates = []

    def make_noise(self):
        return "Woof! Woof!"

    def play_with(self,other):
        if other not in self.playmates:
            self.playmates.append(other)

    def stop_play(self,other):
        if other in self.playmates:
            self.playmates.remove(other)

