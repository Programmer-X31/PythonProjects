import pyperclip
from utils import factorial
import pyinputplus as pyip

num = pyip.inputInt(prompt="Enter a number:   ")


factorial_num = factorial(num)
print(factorial_num)
pyperclip.copy(factorial_num)

print("Factorial Copied to Clipboard")