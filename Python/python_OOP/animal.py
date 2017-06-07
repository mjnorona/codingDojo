class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Health: " + str(self.health)
        return self

animal = Animal("Dog", 15)
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

dog = Dog("Sophia")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
        return self

animal2 = Animal("Bo", 17)
animal2.pet()
animal2.fly()
animal2.displayHealth()

dog.fly()