def enter(phonebook):

    '''This function allow to enter
    name and number in phonebook'''

    name = input('Please enter name ')
    number = input('Please enter number ')
    phonebook[number] = name
    # return phonebook


def output(phonebook):

    '''This function allow to output
    name and number from phonebook'''

    name = input('Please enter name ')
    print('Name       Number')
    if name in phonebook.values():
        for arg in phonebook.items():
            if arg[1] == name:
                print('{0}       {1}'.format(arg[1], arg[0]))
    else:
        print('Sorry, we do not have this person in this phonebook')


def delete():

    '''This function allow to delete name and all numbers
    belong to this name from phonebook'''

    name = input('Please enter name ')
    global phonebook
    if name in phonebook.values():
        phonebook = {i: phonebook[i] for i in phonebook if phonebook[i] != name}
    else:
        print('Sorry, we do not have this person in this phonebook')
    return phonebook


phonebook = {}
Bool = True
print('''
    Please Enter What you want to do?
    If you want enter a new person and his number,write ENTER.
    If you want output numbers of person by his name, please write OUTPUT. 
    If you want delete person, write DELETE
    If you want quit, write QUIT 
    ''')
while Bool:
    command = input('Enter command (ENTER,OUTPUT,DELETE or QUIT) ')

    if command == 'ENTER':
        enter(phonebook)
    elif command == 'OUTPUT':
        output(phonebook)
    elif command == 'DELETE':
        delete()
    elif command == 'QUIT':
        Bool = False
    else:
        print('Sorry, you do not have this option')
