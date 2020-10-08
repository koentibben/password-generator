"""
This module contains the Password Generator
"""

import random

ALL_CHARS = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
NUMBER_OF_PASSWORDS_INPUT = 'INCORRECT'
NUMBER_OF_PASSWORDS_RANGE = range(1, 11)
PASSWORD_LENGTH_INPUT = 'INCORRECT'
PASSWORD_LENGTH_RANGE = range(8, 33)

# check that the number of passwords input is an integer
while not NUMBER_OF_PASSWORDS_INPUT.isdigit():
    NUMBER_OF_PASSWORDS_INPUT = input('How many passwords would you like to generate? (1-10) ')
    if not NUMBER_OF_PASSWORDS_INPUT.isdigit():
        print('Sorry, that is not a digit!')

# check that the number of passwords integer is within the accepted range
while int(NUMBER_OF_PASSWORDS_INPUT) not in NUMBER_OF_PASSWORDS_RANGE:
    print('Sorry, that is not a digit between 1 and 10!')
    NUMBER_OF_PASSWORDS_INPUT = input('How many passwords would you like to generate? (1-10) ')

# check that the password length input is an integer
while not PASSWORD_LENGTH_INPUT.isdigit():
    PASSWORD_LENGTH_INPUT = input('What should be the length of the generated password? (8-32) ')
    if not PASSWORD_LENGTH_INPUT.isdigit():
        print('Sorry, that is not a digit')

# check that the password length integer is within the accepted range
while int(PASSWORD_LENGTH_INPUT) not in PASSWORD_LENGTH_RANGE:
    print('Sorry, that is not a digit between 1 and 32!')
    PASSWORD_LENGTH_INPUT = input('What should be the length of the generated password? (1-32) ')

# generate and print the password(s)
for num in range(int(NUMBER_OF_PASSWORDS_INPUT)):
    PASSWORD = ''
    for char in range(int(PASSWORD_LENGTH_INPUT)):
        PASSWORD += random.choice(ALL_CHARS)
    print('Password: ' + PASSWORD)
