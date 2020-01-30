class Agenda():
    def __init__(self):
        self.contacts = {
            'Anthony': ['Luzquiños', '936962826', 'sluzquinosa@uni.pe'],
            'Rubén': ['Ricapa', '987654321', 'rubenillo@uni.pe']
        }

    def show_contacts(self):
        print('\nContact list:')
        for position, key in enumerate(self.contacts):
            print(position + 1, key, self.contacts[key])
        print()

    def delete_contact(self):
        name = input('Type a name to delete the contact: ')
        self.contacts.pop(name)
        self.show_contacts()

    def search_contact(self):
        name = input('Type a name to search: ')
        if name in self.contacts:
            print('\nContact found:')
            print(name, self.contacts[name])
        else:
            print('The searched contact does not exist')
        print()

    def add_contact(self):
        name = input('Type a name: ')
        lastname = input('Lastname: ')
        cell = self.verify()
        mail = input('Email: ')
        self.contacts[name] = [lastname, cell, mail]
        self.show_contacts()

    def verify(self):
        while True:
            try:
                number = int(input('Type a cellphone number: '))
            except ValueError:
                print('That\'s not a valid cellphone number.')
            else:
                code_validation = self.nine_numbers(number)
                if code_validation == 1:
                    return number
                elif code_validation == 2:
                    print('Error! The cellphone must begin with nine')
                elif code_validation == 3:
                    print('Error! The number must have 9 digits.')
                else:
                    print('Error! The number you\'ve just typed neither has 9 '
                        + 'digits nor begin with nine.')
        
    def nine_numbers(self, number):
        # Codes
        # 1 -> valid number
        # 2 -> it doesn't begin with 9, but it has 9 numbers
        # 3 -> it begins with 9, but it doesn't have 9 numbers
        number = str(number)
        if len(number) == 9 and number[0] == '9':
            return 1  # accepted
        elif len(number) == 9 and number[0] != '9':
            return 2
        elif len(number) != 9 and number[0] == '9':
            return 3
        else:
            return 4

option = ''
agenda = Agenda()

while True:
    print('\nMenu')
    print('1. Show contacts')
    print('2. Add contact')
    print('3. Search contact')
    print('4. Delete contact')
    print('5. Exit')
    option = input('Type an option: ')

    if option == '1':
        agenda.show_contacts()
    elif option == '2':
        agenda.add_contact()
    elif option == '3':
        agenda.search_contact()
    elif option == '4':
        agenda.delete_contact()
    elif option == '5':
        break
    else:
        print('That\'s not a valid option!')