import sys

code_keys = input().split(" ")
if len(code_keys) == 3:
    initiate_stormbreaker()
else: 
    sys.exit()


def initiate_stormbreaker():
    offset = lambda: code_keys[0] if code_keys[0] < 27
    level_of_hash = lambda: code_keys[1] if code_keys[1] < 3
    level_of_encryption = lambda: code_keys[2] if code_keys[2] < 27


    chars = {}
    for i in range(26):
        chars.append()
