from functions import employee


class person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def speak(self):
        print(self.name, "is speaking.")

person1 = person("Mark", 37, "Teacher")
print(person1.name)
person1.speak()

person2 = person("Martha", 35, "Accountant")
print(person2.name)
person2.speak()

