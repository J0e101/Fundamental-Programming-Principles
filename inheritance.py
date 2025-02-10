
#Parent/Super/ Base class
class animal:
    def speak(self):
        print("Animal is speaking.")

#Child/Derived/Sub-class
class dog(animal):
    def bark(self):
        print("Dog is barking")

#Child/Derived/Sub-class
class cat(dog):
    def meow(self):
        print("Cat is meowing")

a = animal()
d = dog()
c = cat()

d.bark()
d.speak()

c.meow()
c.bark()



