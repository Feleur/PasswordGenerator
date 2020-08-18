from random import *
import string
import random


def numberChecker(x, y, z):
    if x+y+z < 8:
        return False


def generator(x, y, z):
    password_list = []
    special = '!@#$%^&*()'

    counter = 1
    counterN = 0
    counterL = 1
    counterS = 0

    # First only letter.
    password_list.append(random.choice(string.ascii_letters))
    while True:
        tmp = randint(0, 3)
        if counterL != x and tmp == 1:
            password_list.append(random.choice(string.ascii_letters))
            counterL = counterL + 1
            counter = counter + 1
        elif counterN != y and tmp == 2:
            password_list.append(randint(0, 9))
            counterN = counterN + 1
            counter = counter + 1
        elif counterS != z and tmp == 3:
            password_list.append(random.choice(special))
            counterS = counterS + 1
            counter = counter + 1
        else:
            continue

        if counter == x + y + z:
            break

    print("Your new password is: " + ''.join(map(str, password_list)) + '\n')

    return password_list


def fileSave(password_list):
    f = open("pwdFile.txt", "w+")
    f.write(''.join(map(str, password_list)) + "\n")
    f.close()
