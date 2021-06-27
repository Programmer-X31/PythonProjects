import random
import os


def factorial(n):
    try:
        """Finds the factorial of a number"""
        if (n == 1):
            return 1
        return n * factorial(n - 1)
        
    except RecursionError:
        for i in range(n, 1, -1):
            return n * i
        
while True:
    try:
        for i in range(13):
            num = str(random.randint(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
        os.system("clear")

        print(num)
    except KeyboardInterrupt:
        break


    
