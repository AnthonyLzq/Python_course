class Agenda():
    def __init__(self):
        self.__conctacts = {
            'Anthony': ['Luzquiños', '936962826', 'sluzquinosa@uni.pe'],
            'Rubén': ['Ricapa', '987654321', 'rubenillo@uni.pe']
        }

    def show_conctacts(self):
        print('\nContact list:')
        for position, key in enumerate(self.__conctacts):
            print(position + 1, key, self.__conctacts[key])
        print()

    def delete_contact(self):
        name = input('Type a name to delete the contact: ')
        self.__conctacts.pop(name)
        self.show_conctacts()

    def search_contact(self):
        name = input('Type a name to search: ')
        if name in self.__conctacts:
            print('\nContact found:')
            print(name, self.__conctacts[name])
        else:
            print('The searched contact does not exist')
        print()

    def add_contact(self):
        name = input('Type a name: ')
        lastname = input('Lastname: ')
        cell = self.__verify()
        mail = input('Email: ')
        self.__conctacts[name] = [lastname, cell, mail]
        self.show_conctacts()

    def __verify(self):
        while True:
            try:
                number = int(input('Type a cellphone number: '))
            except ValueError:
                print('That\'s not a valid cellphone number.')
            else:
                code_validation = self.__nine_numbers(number)
                if code_validation == 1:
                    return number
                elif code_validation == 2:
                    print('Error! The cellphone must begin with nine')
                elif code_validation == 3:
                    print('Error! The number must have 9 digits.')
                else:
                    print('Error! The number you\'ve just typed neither has 9 '
                        + 'digits nor begin with nine.')
        
    def __nine_numbers(self, number):
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