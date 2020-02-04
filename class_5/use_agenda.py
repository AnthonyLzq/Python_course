# import agenda
# import agenda as age
# from agenda import Agenda, COSA_1, COSA_2, ...
from agenda import *

option = ''
agenda_1 = Agenda()

while True:
    print('\nMenu')
    print('1. Show conctacts')
    print('2. Add contact')
    print('3. Search contact')
    print('4. Delete contact')
    print('5. Exit')
    option = input('Type an option: ')

    if option == '1':
        agenda_1.show_conctacts()
    elif option == '2':
        agenda_1.add_contact()
    elif option == '3':
        agenda_1.search_contact()
    elif option == '4':
        agenda_1.delete_contact()
    elif option == '5':
        break
    else:
        print('That\'s not a valid option!')