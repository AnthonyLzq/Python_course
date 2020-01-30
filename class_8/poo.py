# Clase:
#     -> Son abstracciones de las cosas de la vida cotidiana.
#     -> Moldes o plantillas para crear objetos.

# Objeto:
#     -> Un ejemplar de una clase en particular.
#     -> Una instancia de una clase.


class Car():

    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        self.speed = 0
        self.status = 'off'
    
    def turn_on(self):
        if self.status == 'on': 
            print('The car is already turned on.')
        else:
            self.status = 'on'
            print('The car is now turned on.')
    
    def acelerate(self):
        if self.status == 'on':
            self.speed += 10
            print('Now, the speed is:', self.speed)
        else:
            print('The car is turn off, you must turn on it')
    
    def brake(self):
        if self.speed == 0:
            print('The car is already stopped')
        else:
            self.speed = 0
            print('Now, the car has stopped')
    
    def turn_off(self):
        if self.status == 'off': 
            print('The car is already turned off.')
        else:
            self.status = 'off'
            print('The car is now turned off.')

    def __str__(self):
        return 'Modelo: '+self.model+'\nMarca: '+self.brand

car_1 = Car('Grand Prix', 'Pontiac')

print(car_1)
car_1.turn_on()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.brake()
car_1.turn_off()