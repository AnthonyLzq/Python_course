# WHILE

# Factorial de un número de forma descendente:

# while True:

#     num = int(input("Ingresa un número entero para calcular su factorial: "))

#     if num < 0:
#         print("¡Error! El número debe ser positivo o 0.")
#     elif num == 0:
#         print("0! = 1")
#         break
#     else:
#         factorial = num  # Valor del factorial
#         aux = num  # Variable que guarda el valor inicial del número

#         while num > 1:
#             num -= 1
#             factorial = factorial * num

#         print(f'{aux}! = {factorial}')
#         break

# FOR

# range(x) = lista del 0 (<=) a x (<)
# range(x, y) = lista de x (<=) hasta y (<)
# range(x, y, z) = lista de x (<=) hasta y (<) de z en z

# print("Primera forma de range:", end=" ")
# for x in range(10):
#     print(x, end=" ")
# print()

# print("Segunda forma de range:", end=" ")
# for x in range(4, 10):
#     print(x, end=" ")
# print()

# print("Tercera forma de range:", end=" ")
# for x in range(4, 10, 2):
#     print(x, end=" ")
# print()

# print("Range en reversa:", end=" ")
# for x in range(10, 0, -1):
#     print(x, end=" ")
# print()

# name = 'A'

# for char in name:
#     print(char)

# COLECCIONES

#Listas

lista = [1, True, 3.0, 'Anthony', 
            [0, 1, 2.0], False,
            3, 0.5, 'Anchi']
print(lista)
# print(len(lista))
# print(lista[-2:-8:-1])

lista.append('hola',1) # Añade elementos a la lista
print(lista)
lista.pop(1) # Elimina elementos de la lista
print(lista)