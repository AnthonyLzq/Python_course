# Dictionary that represents an agenda

dic = {
    'Anthony': ['Luzquiños', '936962826', 'sluzquinosa@uni.pe'],
    'Rubén': ['Ricapa', '987654321', 'rubenillo@uni.pe']
}

# Codes
# 1 -> valid number
# 2 -> it doesn't begin with 9, but it has 9 numbers
# 3 -> it begins with 9, but it doesn't have 9 numbers

def nine_numbers(number):

    '''
        DOCUMENTACIÓN DE LA FUNCIÓN
    '''
    number = str(number)
    if len(number) == 9 and number[0] == '9':
        return 1 # accepted
    elif len(number) == 9 and number[0] != '9':
        return 2
    elif len(number) != 9 and number[0] == '9':
        return 3
    else:
        return 4


def verify():

    while True:
        try:
            number = int(input('Type a cellphone number: '))
        except ValueError:
            print('That\'s not a valid cellphone number.')
        else:
            code_validation = nine_numbers(number)
            if code_validation == 1:
                return number
            elif code_validation == 2:
                print('Error! The cellphone must begin with nine')
            elif code_validation == 3:
                print('Error! The number must have 9 digits.')
            else:
                print('Error! The number you\'ve just typed neither has 9 '
                        + 'digits nor begin with nine.')


def show_contacts():

    print('Contact list:')
    for position, key in enumerate(dic):
        print(position + 1, key, dic[key])
    print()


def add_contact(name):

    lastname = input('Lastname: ')
    cell = verify()
    mail = input('Email: ')
    dic[name] = [lastname, cell, mail]
    show_contacts()


def search_contact(name):

    if name in dic:
        print('Contact found:')
        print(nombre, dic[nombre])
    else:
        print('The searched contact does not exist')
    print()


def delete_contact(name):
    
    dic.pop(name)
    show_contacts()

contact_name = input('Type a name: ')
add_contact(contact_name)

# Activity:
# 1. Generate a menu with the functions programmed before and it ends when the 
# user types a 0.
# 2. DOCUMENT THE FUNCTIONS WE HAVE HERE.