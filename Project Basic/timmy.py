# Meet Timmy: A simple Timer

import time
import sys
import datetime
from tkinter import *

print(""" 
************************
COMMANDS:
:m => Counts in minutes. (Minimum 1 minute)
:s => Counts in seconds. (Minimum 1 second)
:h => Counts in hours.   (Minimum 1 hour)
:e => Exit
************************
:""", end="")
command = input()


def main():
    if command == "m":
        targeted_time = int(input("\nEnter a time(minutes) \n")) * 60
        process_input(targeted_time)
    elif command == "s":
        targeted_time = int(input("\nEnter a time(seconds) \n"))
        process_input(targeted_time)
    elif command == "h":
        targeted_time = int(input("\nEnter a time(hours) \n")) * 3600
        process_input(targeted_time)

    else:
        print("Code Terminated")
        sys.exit()


def process_input(t):
    for i in range(t, 1, -1):
        if i < 61:
            print(str(i) + " seconds")
            time.sleep(1)
        else:
            time_taken = (f'{int(i/60)} min  {int(i % 60)} seconds')
            print(time_taken)
            time.sleep(1)
    print(f'Code Completed at: \n\t{datetime.datetime.now()}')


try:
    main()
except KeyboardInterrupt:
    sys.exit()
