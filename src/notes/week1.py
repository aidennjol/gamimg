# Basic programming cycle
    # Design the code
        # Plan how your gonna approach
        # Gather requirements
        # Think about tools and shit
    # Writing the code
        # Getting the core functionality
        # Scaffolding
        # Minimal Viable Product (how little work can I do and still satisfy the requirments)
    # Correct Syntax Errors
        # Running your code
        # Fixing why it doesnt run or execute
    # Testing the program
        # Test use cases (these are usually part of the requirements that have been gathered)
        # Write unit tests and regression tests
        # Try to break things
        # Fix Bugs (things that dont work as they should/break/you have missed)
    # Rinse and repeat
        # At university this means finishing the core assignment FIRST and then any addition bonus questions second
        # In the workplace this means continuing to add code and build the product until the contract expires or the client is happy


# Pseudocode
# The idea that code can be expressed in laymans terms and you can understand the meaning
#  is an informal language used to develop a program’s design. It has no syntax rules and is not meant to be compiled or executed. 
# EG

"""
    while all of a man's dogs haven't been fed
        open a can of dog food
        fill a bowl
        let dog eat food
        if all dogs have finished eating
            stop feeding dogs
"""

# Naming python variables

# good
temp_name = 'Danny'
def calculate_wage():
    pass

this_is_a_long_example = '123'

# bad
aVariable = 123
VaRiaBLe = 123
nospacename = 'bad'
a = 'this is bad contextually'
# other bad names include python keywords like map, list, error, def, etc etc et
# list = 123        (EXTREMELY BAD)

# however sometimes you need to name a variable after a keyword or a predefined function
_list = 'this is fine'
__temp = 'this is also fine'

# in summary
    # no keywords
    # no spaces
    # lowercase letters only
    # can use _ and numbers
    # must start with a letter

# Constants and variables
this_is_a_variable = 'you can change me'
THIS_IS_A_CONSTANT = 'you cant change me'
# later in code
this_is_a_variable = 'ive been changed'
# THIS_IS_A_CONSTANT = 'ive been changed' NOT ALLOWED

MEEPO_ABSOLUTE_MAX_CLONES = 5
meepo_current_max_clones = 4

# buys aghs
meepo_current_max_clones = 5
print('Variable examples')
print(MEEPO_ABSOLUTE_MAX_CLONES)
print(this_is_a_variable)


# Math Operators
print(f'\nMath Operator Examples')
print(f'3+3 = {3+3}') # + operator adds things (6)
print(f'3-3 = {3-3}') # - operator subtracts things (0)
print(f'3*3 = {3*3}') # + operator multiplys things things (9)
print(f'30/4 = {30/4}') # + operator divides things and makes them a float (7.5)
print(f'30//4 = {30//4}') # divides and rounds down (7)
print(f'30%4 = {30%4}') # returns the remainder of rounded division (2) (called modulus)

# Boolean operators
# > Greater than (eg 5 > 4 = True)
# < Less than (eg 2 < 1 = False)
# >= Greater than or equal to (eg 2 >= 2 = True)
# <= less than or equal to (eg 3 <= 3 = True)
# == (Double Equals)
print('\nDouble Equals (==) examples')
print(f'True == True solves to {True == True}')
print(f'True == False solves to {True == False}')
print(f'"tom" == "tom" solves to {"tom" == "tom"}')
print(f'3 == 4 solves to {3 == 4}')
# Double equals compares two things and gives True if they are exactly the same
# != (not equal)
print('\nNot Equals (!=) examples')
print(f'True != True solves to {True != True}')change_me > 5:
    print('The variable has been set to a number larger than 5')
elif change_me == 5:
    print('The variable has been set to 5')
elif change_me < 5 and change_me > 0:
    print('The variable is less than 5 but greater than 0')
else:
    print('Logically the number must be less than 0')

print(f'True != False solves to {True != False}')
print(f'"tom" != "tom" solves to {"tom" != "tom"}')
print(f'3 != 4 solves to {3 != 4}')

# GOTCHA: "3" != 3 because "3" is a string and 3 is an integer

# Boolean Expressions
# A boolean expression will either be True (1) or False(Anything but 1, usually 0)
# The bool() function converts ANY value to a true or false where applicable
# Using boolean math, we can solve boolean equations
# Eg
print('\nBoolean Examples')
print(f'True = {True}')
print(f'1 = {bool(1)}')
print(f'False = {False}')
print(f'0 = {bool(0)}')

# There are also boolean operators (https://introcs.cs.princeton.edu/java/71boolean/images/truth-table.png)
# The basic ones are
# and
print('\nAND examples')
print(f'True and True = {True and True}')
print(f'True and False = {True and False}')
print(f'False and False = {False and False}')
# an AND only equals true if both sides are true

# or
print('\nOR examples')
print(f'True or True = {True or True}')
print(f'True or False = {True or False}')
print(f'False or False = {False or False}')
# an OR only equals true if at least ONE side is true

# not
print('\nNOT examples')
print(f'not True = {not True}')
print(f'not False = {not False}')
# A not always makes its partner the opposite

# ^ XOR (used only sometimes)
print('\nXOR (^) examples')
print(f'True ^ True = {True ^ True}')
print(f'True ^ False = {True ^ False}')
print(f'False ^ False = {False ^ False}')change_me > 5:
    print('The variable has been set to a number larger than 5')
elif change_me == 5:
    print('The variable has been set to 5')
elif change_me < 5 and change_me > 0:
    print('The variable is less than 5 but greater than 0')
else:
    print('Logically the number must be less than 0')

# A XOR is true if both sides are different

# Boolean can be chained many times to equate to one final answer just like math
# eg
print('Large boolean example')
print(f'(True or False) and True = {(True or False) and True}')
# Just like math the brackets go first
# True or False is solved first (= True)
# The equation then becomes True and True which solves to = True
print(f'not(True and False) or False = {not(True and False) or False}')
# Brackets first (True and False) = False
# New equations is not False or False
# No more brackets, invert the nots
# New equations is True or False
# True or False solves to True

# Conditional Statements
# The reason we use boolean is so python can _sometimes_ execute code depending on whether things are true or false
# We do this using if, else and elif (else if) statements
# change the varible below to get different results

change_me = -1

if change_me > 5:
    print('The variable has been set to a number larger than 5')
elif change_me == 5:
    print('The variable has been set to 5')
elif change_me < 5 and change_me > 0:
    print('The variable is less than 5 but greater than 0')
else:
    print('Logically the number must be less than 0')


