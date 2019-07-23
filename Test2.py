class Animal:

    def talk(self, animal):
        animal.speak()


class Cat(Animal):

    def speak(self):
        print("Meow meow")

class Dog(Animal):

    def speak(self):
        print("Bark bark")


hund = Animal()
cato = Animal()
hund.talk(Dog())
cato.talk(Cat())

