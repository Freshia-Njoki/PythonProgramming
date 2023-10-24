# Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("cat is meowing")

d = Dog()
d.speak()

c = Cat()
c.meow()