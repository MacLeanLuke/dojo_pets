from pet_class import Pet

# Create a Ninja class with the ninja attributes listed above.
class Ninja():
    # implement __init__( first_name , last_name , treats , pet_food )

    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet(name='', type='', tricks='', sound='')
        self.treats = treats
        self.pet_food = pet_food
    
    # implement the following methods:
    def adopt_a_pet(self, name, type, trick, sound):
        self.pet.name = name
        self.pet.type = type
        self.pet.tricks = trick
        self.pet.sound = sound

    def ninja_and_pet_display(self):
        return "my name is {} and I have a pet named {} she has {} energy".format(self.first_name, self.pet.name, self.pet.energy)

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()


    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()


    def bathe(self):
        self.pet.sound()