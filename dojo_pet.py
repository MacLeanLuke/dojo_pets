# NINJA BONUS: Use modules to separate out the classes into different files.

from ninja_class import Ninja

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
ninja1 = Ninja('joe','shmoe','salmon snacks','Victor')
ninja1.adopt_a_pet('winnie','golden','shake','bark')

# Implement walk(), feed(), bathe() on the ninja class.
# Have the Ninja feed, walk , and bathe their pet.
# ninja1.walk()
# ninja1.feed()
# ninja1.bathe()

# Implement sleep(), eat(), play(), noise() methods on the pet class.
# ninja1.pet.sleep()
# ninja1.pet.eat()
# ninja1.pet.play()
# ninja1.pet.noise()

print(ninja1.ninja_and_pet_display())