# Functions

number = 27
print('Number from outside:', number)

def greet(name, age):
    global number
    number += 2 # numero = numero + 2
    print('Number from greet:', numero)
    # print(f'Hi {name}! You  are {age} years old!')
    return number

def leave():
    # number2 = number
    number += 2 # number = number + 2
    print('Number from leave:', number)
    # print('Nos vemos!')

greet('Anthony', 23)
print('Number from outside:', number)
# salir()
