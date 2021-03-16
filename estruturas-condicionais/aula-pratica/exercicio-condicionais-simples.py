'''
    - Translate the following statements into Python conditionals:
    a) If age is over 60, write: "you have rights to benefits"
    b) If damage is greater than 10 and shield is equal to 0, write: "you are dead!"
    c) If at least one of the North, South, East and West Boolean variables
     result in True, write: "You escaped"
'''

age = int(input('Enter your age: _'))

if (age > 60):
    print('You have rights to benefits')

damage = int(input('Damage: _'))
shield = int(input('Shield: _'))

if ((damage > 10) and (shield == 0)):
    print('You are is dead')

north = False
south = True
east = False
west = False

if (north or south or east or west):
    print('You escaped')


'''
    - Translate the following statements into Python conditionals:
    a) If the year is divisible by 4, write: "It can be a leap year". 
    Otherwise, write: "It is definitely not a leap year"
    b) If both the up and down Boolean variables are True, write: 
    "Make up your mind", otherwise, write: "You chose a path!"
'''

year = int(input('Enter a year: _'))
if (year % 4):
    print('It can be a leap year')
else:
    print('It is definitely not a leap year')


up = True
down = False

if (up and down):
    print('Make up your mind')
else:
    print('You chose a path!')
