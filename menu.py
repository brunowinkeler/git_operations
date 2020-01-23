## @package menu.py
#  Create a personalized menu to call other features routines
#
#  With this code it is possible to integrate all features developed
#    in an only one menu.

import os

os.system('cls')

# Logo ##############################################################

print('_'*95)

file_ = open('./utils/logo.txt', 'r')

for line_ in file_:
    print(line_.replace('\n',''))

print('_'*95)


# MENU ###################################################################

print("\nWhich of the following options would you like to run?\n".upper())

print('1 - Update to Hash')
print('2 - Generate Log [NOT AVAILABLE]')
print('3 - Compile All [NOT AVAILABLE]')

ans_ = input('\nType your answer: '.upper())

print('\n')

if(ans_ == '1'):
    os.system('python ./update_to_hash/update_to_hash.py')





