import time
import sys

try:
    time_taken = 0
    while True:
        time.sleep(1)
        time_taken += 1
except KeyboardInterrupt:
    print(f'{time_taken // 60} mins {time_taken % 60} secs')
    print("Code Completed")
    sys.exit()
