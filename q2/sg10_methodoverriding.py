class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return f"{self.name} roars loudly!"

    def eat(self):
        return f"{self.name} eats fresh meat."

class Elephant(Animal):
    def make_sound(self):
        return f"{self.name} trumpets!"

    def eat(self):
        return f"{self.name} eats grass and fruits."

class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} chatters!"

    def eat(self):
        return f"{self.name} eats bananas."

Lion1 = Lion("Simba")
Elephant1 = Elephant("Dumbo")
Monkey1 = Monkey("George")

print(Lion1.make_sound())
print(Lion1.eat())
print("-----")

print(Elephant1.make_sound())
print(Elephant1.eat())
print("-----")

print(Monkey1.make_sound())
print(Monkey1.eat())
print("-----")

