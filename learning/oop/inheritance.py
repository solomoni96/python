class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    def show(self):
        print(f"I am {self.name}! I'm {self.age} years old")
        
    def speak(self):
        print('...')
        
class Dog(Pet):
    def speak(self):
        print('woof!')

class Cat(Pet):
    def __init__(self, name, age, colour):
     super().__init__(name, age)
     self.colour = colour
     
    def show(self):
        print(f"I am {self.name}! I'm {self.age} years old and {self.colour}")
        
    def speak(self):
        print('Meow!')
        self.show()

class Dog(Pet):
    def speak(self):
        print('woof!')
        
        
p = Pet('Joe', 12)
p.show()
p.speak()

d = Dog('Max', 14)
d.show()
d.speak()
        
c = Cat("Toby", 6, "red")
c.speak()
