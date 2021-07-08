
# Create a Pet class with the pet attributes listed above.

class Pet():
    # implement __init__( name , type , tricks , sound):
    def __init__(self, name , type , tricks, sound):

        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 0
        self.energy = 0


    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5

    # noise() - prints out the pet's sound
    def noise(self):
        return self.sound

    def display_pet_info(self):
        pass
        # return f"Pet: {self.name}"