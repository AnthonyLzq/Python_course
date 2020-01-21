# WHILE

# FACTORIAL DESCENDENTE

# answer = ''
# num = 0
# factorial = 1
# aux = num

# while True:
#     num = int(input('Type a number: '))
#     if num < 0:
#         print('Error! The number must be positive or 0!')
#     else:
#         aux = num
#         while num > 0:
#             factorial *= num # factorial = factorial * num
#             num -= 1

#         print(f'{aux}! = {factorial}')

#         while answer != 'y' or answer != 'n':
#             answer = input('Have you finished? (y/n)')
#             if answer != 'y' and answer != 'n':
#                 print('Error! The value must be y or n.')
#             else:
#                 break

#         if answer == 'y':
#             break
#         else:
#             factorial = 1

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

# Listas

# lista = [1, True, 3.0, 'Anthony', [0, 1, 2.0], False, 3, 0.5, 'Anchi']
# print(lista)
# # print(len(lista))
# # print(lista[-2:-8:-1])

# lista.append('hola',1) # Añade elementos a la lista
# print(lista)
# lista.pop(1) # Elimina elementos de la lista
# print(lista)

# Tuplas

# tupla = (1.0, 2.0, 'Anthony', True, 1, 1, 1, 1.0)

# for value in tupla:
#     print(value, end=' ')
# print()

# print(tupla)
# lista = list(tupla)
# lista = tuple(lista)
# print(lista)

# Conjuntos

# A = set()
# A = {1, 2, 3, 1, 2, 3, 4, 5, 4, 5}
# print(type(A))
# print(A)
# A.add(6)
# print(A)
# A.discard(1)
# print(A)
# A.discard(1)
# print(A)
# A.remove(1)
# print(A)
# B = set()
# B = {4, 5, 6, 7}

# C = A | B # Unión
# print(C)
# C = A & B # Intersección
# print(C)
# C = A ^ B # Dif. simétrica
# print(C)
# C = A - B
# print(C)

# print(A.isdisjoint(B))
# print(A.issubset(B))
# print(A.issuperset(B))

# Diccionarios

dic = {'Anthony': 'Luzquiños', 'Alvaro': 'Plasencia',
        'Rubén': 'Ricapa', 'Esteban': 'Figueroa'}
# print(dic)
# keys = list(dic.keys())
# values = list(dic.values())
# print(keys)
# print(values)

for x, key in enumerate(dic):
    print(x + 1, key)

dic['Carlos'] = 'Bazán'
print(dic)
dic.pop('Alvaro')
print(dic)