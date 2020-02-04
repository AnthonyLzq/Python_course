class Vehicle():
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
        self.isOn = False
        self.isMovement = False

    def __str__(self):
        data = '\nBrand: ' + self.brand + '\nModel: ' \
            + self.model+'\n'
        return data
    
    def acelerate(self):
        # Codes:
        # 1 -> It's turned on and is in movement.
        # 2 -> It's turned on, but is quiet.
        # 3 -> It's turned off
        if self.isOn and self.isMovement:
            return 1
        elif self.isOn:
            return 2
        else:
            return 3

    def turn_on(self):
        self.isOn = True

    def move(self):
        # Code:
        # 1 -> Now, it's in movement
        # 2 -> It isn't turned on
        if self.isOn:
            self.isMovement = True
            return 1
        else:
            return 2


class Motorcycle(Vehicle):

    def acelerate(self):
        code = super().acelerate()
        if code == 1:
            self.speed += 7
            print(f'Now, the speed is: {self.speed}m/s.')
        elif code == 2:
            print('You must start the movement.')
        else:
            print('You must turn on the motorcycle.')

    def turn_on(self):
        super().turn_on()
        print('Now, the motorcycle is turned on.')

    def move(self):
        code = super().move()
        if code == 1:
            print('The motorcycle is now in movement.')
            self.acelerate()
        else:
            print('The motorcycle can\'t move because is turned off.')

    def __str__(self):
        data = super().__str__()
        if self.isOn:
            data += 'The motorcycle is in movement.'
            if self.isMovement:
                data += '\nThe speed is ' + str(self.speed) + 'm/s.'
        return data


class Car(Vehicle):

    def __init__(self, brand, model, type, number_doors=4):
        super().__init__(brand, model)
        self.number_doors = number_doors
        self.type = type
    
    def acelerate(self):
        code = super().acelerate()
        if code == 1:
            self.speed += 10
            print(f'Now, the speed is: {self.speed}m/s.')
        elif code == 2:
            print('You must start the movement.')
        else:
            print('You must turn on the car.')

    def turn_on(self):
        super().turn_on()
        print('Now, the car is turned on.')

    def move(self):
        code = super().move()
        if code == 1:
            print('The car is now in movement.')
            self.acelerate()
        else:
            print('The car can\'t move because is turned off.')

    def __str__(self):
        data = super().__str__()
        data += 'The type is: ' + self.type + '\n' \
                + 'The doors number is: ' + self.number_doors + '\n'
        if self.isOn:
            data += 'The car is in movement.'
            if self.isMovement:
                data += '\nThe speed is ' + str(self.speed) + 'm/s.'
        return data

    
