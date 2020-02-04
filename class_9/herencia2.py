import random


class Animal():
    def __init__(self, species='Unknown', name='Unknown',\
            size='Unknown', onomatopoeia='Unknown',\
            age='Unknown', gender='Unknown'):
        self.species = species
        self.name = name
        self.size = size
        self.onomatopoeia = onomatopoeia
        self.age = age
        self.isMovement = False
        if gender == 'Unknown':
            prob = random.randint(0, 1)
            if prob == 0:
                self.gender = 'Female'
            else:
                self.gender = 'Male'
        else:
            self.gender = gender

    def move(self):
        self.isMovement = True
    
    def sound(self):
        print(self.onomatopoeia)

    def __str__(self):
        data = 'Species: ' + self.species + '\n' + \
            'Name: ' + self.name + '\n' + \
            'Size: ' + self.size + '\n' + \
            'Onomatopoeia: ' + self.onomatopoeia + '\n' + \
            'Age: ' + str(self.age) + '\n' + \
            'Movement: ' + str(self.isMovement) + '\n' + \
            'Gender: ' + self.gender + '\n'
        return data


class Cat(Animal):
    def __init__(self, name, age, gender, size='small'):
        super().__init__('Cat', name, size, 'Miau', age, gender)


class Dog(Animal):
    def __init__(self, name, age, gender, size='small'):
        super().__init__('Dog', name, size, 'Guau', age, gender)


animal_1 = Animal(species='cat',onomatopoeia='Muuuu')
print(animal_1)

dog_1 = Dog('Ringo', 4,'male', 'medium')
print(dog_1)

dog_2 = Dog('Churra', 3, 'female', 'medium')
print(dog_2)

cat_1 = Cat('Ema', 0.5, 'female')
print(cat_1)
