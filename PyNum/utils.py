import time
import pyperclip

def isEven(n):
	if n % 2 == 0:
		return "Even"
	else:
		return "Odd"
	
def isPrime(n) : 
 
    if (n <= 1) : 
        return "Not Prime"
    if (n <= 3) : 
        return "Prime"
 
    if (n % 2 == 0 or n % 3 == 0) : 
        return "Not Prime"
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return "Not Prime"
        i = i + 6
 
    return "Prime"


def factorial(n):
    try:
        """Finds the factorial of a number"""
        if (n == 1):
            pyperclip.copy(str(factorial(n)))
            return 1
        return n * factorial(n - 1)
        
    except RecursionError:
        for i in range(n, 1, -1):
            return n * i
        pyperclip.copy(str(factorial(n)))
        

def print_multiples(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {str(n * i)}")
        time.sleep(1)

def print_factors(n):
    for i in range(1, n // 2):
        if (n % i) == 0:
            print(f"{i}    {int(n / i)}")
            time.sleep(1)

