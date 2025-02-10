class employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def details(self):
        print(self.name, "is the", self.position)

employee1 = employee("John", 450000, "CEO")
employee2 = employee("Jane", 350000, "Managing Director",)
employee3 = employee("Eunice",465000,"HR")

print(employee1.name, employee1.position, employee1.salary)
employee2.details()

