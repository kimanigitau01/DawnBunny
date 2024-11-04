class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def movement(self):
        print(self.name.title(), "is walking.")



acc = Person("joe", 34, "male")
bee = Person("Alice", 29, "female")
cat = Person("Charles", 54, "male")

acc.movement()
print(cat.age)