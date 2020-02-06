# import sys
# print('tú')

from io import open

# Crear y abrir
# file_1 = open('test.txt', 'w')
# file_1.close()
file_1 = open('test.txt', 'r+') 
'''
    Tipo escritura: 
        w -> crea el archivo y si existe, lo abre en modo escritura y lo chanca.
    Tipo lectura: 
        r -> abre en modo lectura.
    Tipo append: 
        a -> abre el archivo y escribe al final.

    Tipo lectura-escritura:
        r+ -> abre en modo lectura-escritura, sin chancarlo.
    Tipo escritura-lectura:
        w+ -> crea el archivo y si existe, lo abre en modo lectura-escritura, y lo chanca.
'''

# Manipular
string = file_1.read()
# file_1.seek(0)
# string = file_1.read()

print(string)
file_1.write('Bye Rubén\n')
file_1.seek(0)
lines = file_1.readlines()

for i in range(0, len(lines)):
    lines[i] = lines[i].rstrip('\n')

# Cerrar
file_1.close()
print(f'lines:\n{lines}')

