'''
NOTE: THIS PROGRAM REQUIRES PILLOW LIBRARY , PLEASE INSTALL PIL
To install pil:
open cmd -> cd appdata -> cd local -> cd programs -> cd python ->
cd python[enter the version of your python software] (eg : cd python39 for ver 3.9) ->
cd scripts -> pip install pillow -> pillow library will be installed
if you have a customized location for python please use that file location
'''

# imports for diff purpose
import sys
from sys import stdout
# try-except is used to avoid errors in case the user hasn't downloaded the PIL library
try:
    from PIL import Image
except ModuleNotFoundError:
    exit('Please install PIL')
from time import sleep
#...


# the images requires for the code:
and_ = Image.open('AND.png')
or_ = Image.open('OR.png')
not_ = Image.open('NOT.png')
nand_ = Image.open('NAND.png')
nor_ = Image.open('NOR.png')
xor_ = Image.open('XOR.png')
xnor_ = Image.open('XNOR.png')
all_=Image.open('logic gates.png')
# ...


# typing animation
def pprint(message):
    for letter in message:
        stdout.write(letter)
        stdout.flush()
        sleep(0.05)
    stdout.write('\n')    
#...


# introduction
def intro():
    pprint('\n'*3)
    pprint('Welcome\n')
    pprint('This is a program to learn logic gates.\n')
    pprint('Logic gates are the basic building blocks of any digital system')
    pprint('It is an electronic circuit having one or more than one input and only one output')
    pprint('The relationship between the input and the output is based on a certain logic\n')
    pprint('These are the different types of logic gates: ')
    menu()
    choice()
#...


# menu options
def menu():
    sleep(1)
    print('\n1.AND gate')
    print('2.OR gate')
    print('3.NOT gate')
    print('4.NAND gate')
    print('5.NOR gate')
    print('6.XOR gate')
    print('7.XNOR gate')
    print('8.All the gates\n')
    print('9.[END]\n')
    sleep(1)
# ...


# choices for the user
def choice():
    c = input('To learn about any specific logic gate type the corresponding number :')
    while c not in ['1', '2', '3', '4', '5', '6','7','8','9']:
        pprint('Please enter a valid option')
        c = input('To learn more about any specific logic gate type the corresponding number :')
    if  c == '1':
        AND()
    elif c == '2':
        OR()
    elif c == '3':
        NOT()
    elif c == '4':
        NAND()
    elif c == '5':
        NOR()
    elif c == '6':
        XOR()
    elif c == '7':
        XNOR()
    elif c == '8':
        sleep(1)
        all_.show()
    elif c == '9':
        pprint('\nThank you\n')
        sys.exit()
# ...


# all the definitions of logic gates
def AND():
    pprint('AND gate :')
    pprint('The AND gate gives a high output (1) only if all its inputs are high. A dot (.) is used to show the AND operation i.e. A.B')
    sleep(3)
    and_.show()


def OR():
    pprint('OR gate :')
    pprint('The OR gate gives a high output (1) if one or more of its inputs are high. A plus (+) is used to show the OR operation i.e. A+B')
    sleep(3)
    or_.show()


def NOT():
    pprint('NOT gate :')
    pprint("The NOT gate  produces an inverted version of the input as its output. It is also known as an inverter")
    pprint("If the input variable is A, the inverted output is known as NOT A. This is also shown as A' or A with a bar over the top")
    sleep(5)
    not_.show()


def NAND():
    pprint('NAND gate :')
    pprint('This is a NOT-AND gate which is equal to an AND gate followed by a NOT gate. The output of NAND gate is high if any of the inputs are low')
    pprint('The symbol is an AND gate with a small circle on the output. The small circle represents inversion.')
    sleep(5)
    nand_.show()


def NOR():
    pprint('NOR gate :')
    pprint('This is a NOT-OR gate which is equal to an OR gate followed by a NOT gate. The outputs of all NOR gates are low if any of the inputs are high')
    pprint('The symbol is an OR gate with a small circle on the output. The small circle represents inversion')
    sleep(5)
    nor_.show()


def XOR():
    pprint('XOR gate :')
    pprint('The "Exclusive-OR" gate is a circuit which will give a high output if either, but not both of its two inputs are high')
    sleep(3)
    xor_.show()


def XNOR():
    pprint('XNOR gate :')
    pprint('The "Exclusive-NOR" gate circuit does the opposite to the XOR gate. It will give a low output if either, but not both of its two inputs are high')
    pprint('The symbol is an XOR gate with a small circle on the output. The small circle represents inversion')
    sleep(5)
    xnor_.show()
# ...


# program was created by:
def credits():
    cred = input('View credits? (y/n): ')
    while cred not in ['y','n']:
        pprint('Please enter valid option')
        cred = input('View credits? (y/n): ')
    if cred == 'y':
        pprint('The program was created by :\n')
        pprint('KR.Bala')
        pprint('Varsha NK')
        pprint('Nayana')
        pprint('Varun')  
#...


# displaying the intro , menu and choices
intro()
while True:
    again_ = input('Do you want to learn about another gate? (y/n): ')
    while again_ not in ['y', 'n']:
            pprint('please enter valid option (y/n)')
            again_ = input('Do you want to learn about another gate? (y/n): ')
    if again_ == 'y':
        menu()
        choice()
    else:
        credits()
        pprint('\nThank you\n')
        break
#...
       
