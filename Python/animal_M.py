class Animal:
    def __init__(self,name,health):
        self.name = name
        self.health=health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health=self.health-5
        return self
    def display_health(self):
        print("The current health is at {}".format(self.health))
class Dog(Animal):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.health=150
    def pet(self):
        self.health+=5
        return self
class Dragon(Animal):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.health=170
    def fly(self):
        self.health-=10
        return self
    def display_health(self):
        Animal.display_health(self)
        print("I am a Dragon")
class Cat(Animal):
    def __init__(self,name,health):
        super().__init__(name,health)
    def purr(self):
        self.health+=20
        return self
example=Animal("jaguar",60).walk().walk().walk().run().run().display_health()
puppy=Dog("snowball",60).walk().walk().walk().run().run().pet().display_health()
drag=Dragon("Eragon",60).fly().display_health()
kitten=Cat("Mr. Kitty",50).purr().display_health()