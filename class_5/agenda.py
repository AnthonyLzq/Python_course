# Dictionary that represents an agenda
dic = {
    'Anthony': ['Luzquiños', '936962826', 'sluzquinosa@uni.pe'],
    'Rubén': ['Ricapa', '987654321', 'rubenillo@uni.pe']
}


def show_contacts():

    print('Contact list:')
    for position, key in enumerate(dic):
        print(position + 1, key, dic[key])
    print()


def add_contact(name):

    lastname = input('Lastname: ')
    cell = input('Cellphone number: ')
    mail = input('Email: ')
    dic[name] = [lastname, cell, mail]
    mostrar_contacos()


def search_contact(name):

    if name in dic:
        print('Contact found:')
        print(nombre, dic[nombre])
    else:
        print('The searched contact does not exist')
    print()


def delete_contacto(name):
    
    dic.pop(name)
    show_contacts()

# Activity:
# Generate a menu with the functions programmed before and it ends when the 
# user types a 0.