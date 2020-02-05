# x = 10
# print(type(x))
# x += 1 # x = x + 1
# print(x)
# x -= 1 # x = x - 1
# print(x)
# x /= 3 # x = x/3
# print(x)
# x *= 3 # x = x*3
# print(x)
# print(type(x))

# name = 'Anthony'
# age = 23
# # print(len(name))
# print(name, 'is', age, 'years old.')
# print('{} is {} years old.'.format(name, age))
# print(f'{name} is {age} years old.')

# v = 3 < 3
# print(v)
# v = 3 > 1
# print(v)
# # print(type(v))
# v = (not 5 < 10) or 3 > 5
# print(v)

# name = input('What\'s your name? ')
# age = int(input(f'Hi {name}, how old are you? '))

# if age < 0:
#     print('Error! An age can\'t be negative.')
# elif age < 18:
#     print('You shall not pass.')
# else:
#     print('You are allowed to pass.')

char = input('Type a letter: ').lower()
# print(char)
if len(char) == 1:
    if char == 'a' or char == 'e' or char == 'i'\
        or char == 'o' or char == 'u':
        print('The letter you have typed is a vowel.')
    else:
        print('The letter you have typed is not a vowel.')
else:
    print('You must type a letter.')