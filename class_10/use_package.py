# import vehicles
# import vehicles as vhcs
# from vehicles import Motorcycle, Car
from classes.vehicles import *
from classes.animals import *

moto_1 = Motorcycle('Susuki', 'BM3')
# print(moto_1)

moto_1.turn_on()
moto_1.move()
moto_1.acelerate()
print(moto_1)

car_1 = Car('Pontiac', 'Grand Prix', 'manual', '2')
print(car_1)

cat_1 = Cat('Ema', 0.5, 'female')
print(cat_1)

dog_1 = Dog('Ringo', 4,'male', 'medium')
print(dog_1)

animal = Animal(onomatopoeia='Beeeeee')
print(animal)