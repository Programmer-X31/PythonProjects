import time
import math
from getpass import getpass
from colorama import init
from colorama import Fore, Style

init()

# Input
num = int(input("Enter a number \n"))


def check(n):
    if n > 1:
        for i in range(n):
            if n % i == 0:
                print("Prime")
                break
            else:
                print("Not Prime")


def is_perfect_cube(x):
    x = abs(x)
    return int(round(x ** (1.0 / 3))) ** 3 == x


text = open("secret.txt", "r")
checked_password = text.read()
password = getpass("Enter Password \n")
access_granted = False

if password == checked_password:
    access_granted = True
else:
    print(Fore.RED + "\n-------ACCESS TERMINATED-------")
    print(Style.RESET_ALL)


while access_granted:
    print(Fore.GREEN + "-------ACCESS GRANTED-------\n")
    print(Style.RESET_ALL)
    time.sleep(3)
    print("\n---------------PROPERTIES-----------------")
    time.sleep(1)
    even = False
    # Finding out if it is even
    if num % 2 == 0:
        even = True
        print("Even/Odd:      EVEN")
        time.sleep(1)
    else:
        even = False
        print("Even/Odd:      ODD")
        time.sleep(1)
    # Finding out if it is prime
    if check(num):
        print("Is Prime:      PRIME")
        time.sleep(1)
    else:
        print("Is Prime:      NOT PRIME")
        time.sleep(1)
    # Square
    square = str(num ** 2)
    print("Square:        " + square)
    time.sleep(1)
    # Cubes
    cube = str(num ** 3)
    print("Cube:          " + cube)
    time.sleep(1)
    # Square Root
    square_root = math.sqrt(num)
    print("Square Root:   " + str(int(square_root)))
    time.sleep(1)
    print("Perfect Cube:  " + str(is_perfect_cube(num)).upper())
    time.sleep(1)
    if is_perfect_cube(num):
        for ans in range(0, abs(num) + 1):
            if ans ** 3 == abs(num):
                break
            if ans ** 3 != abs(num):
                print(num, "is not a perfect cube!")
            else:
                if num < 0:
                    ans = -ans
                print("Cube root:" + str(ans))
                time.sleep(1)
    else:
        print("Cube root:     None")
        time.sleep(1)
    print("\n---------------MULTIPLES------------------")
    multiples = []
    print("Multiples:")
    time.sleep(0.75)
    for i in range(10):
        multiples.append(num * i)
        if i < 9:
            print(
                str(num)
                + " x "
                + str(0)
                + str(int(i + 1))
                + "  =  "
                + str(int(multiples[i] + num))
            )
            time.sleep(1)
        else:
            print(
                str(num)
                + " x "
                + str(int(i + 1))
                + "  =  "
                + str(int(multiples[i] + num))
            )
            time.sleep(1)
    print("\n---------------POWERS------------------")
    for i in range(11):
        power = num ** i
        print(str(num) + "**" + str(i) + " = " + str(power))
        time.sleep(1)
    print("\n---------------FACTORS------------------")
    factors = []
    for i in range(num):
        if num % (i + 1) == 0:
            factors.append(i + 1)
            factors.append(num / (i + 1))
            factors.sort()
    factors_revised = list(set(factors))
    for factor in factors_revised:
        factors_revised.sort()
        print(str(int(factor)) + " (x " + str(int(num / factor)) + ")")
        time.sleep(1)