import pyinputplus as pyip
from utils import isEven, isPrime, factorial, print_factors, print_multiples
import time
import sys

num = pyip.inputInt(prompt="Enter a number:   ")
# Can:
#   -> Square Numbers
#   -> Cube Numbers
#   -> Tell Factors
#   -> Multiples
#   -> Prime Number or not
#   -> Even/ Odd

def initiate():
	print("-------PROPERTIES--------\n\n")
	time.sleep(1)
	print(f"Even/Odd:           {isEven(num)}")
	time.sleep(1)
	print(f"Prime/Not Prime:    {isPrime(num)}")
	time.sleep(1)
	print(f"Factorial:          {factorial(num)}")
	time.sleep(1)
	print(f"Square:             {num * num}")
	time.sleep(1)
	print(f"Cube:               {num ** 3}")
	time.sleep(1)
	
	print("\n\n-------MULTIPLES-------\n\n")
	time.sleep(1)
	print_multiples(num)
	
	time.sleep(1)
	print("\n\n-----FACTORS------\n\n")
	time.sleep(1)
	print_factors(num)



	print("Copied Factorial to Clipboard!!")

try:
	initiate()
except KeyboardInterrupt:
	sys.exit()
