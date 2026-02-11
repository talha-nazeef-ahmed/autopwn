#!usr/bin/env python3
import string


def pattern_generator(length):
    pattern = ""
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    for i in upper:
        for j in lower:
            for k in numbers:
                seq = i + j + k
                pattern += seq
                if len(pattern) >= length:
                    return pattern[:length]
    return pattern[:length]


def position_finder(pattern, value):
    found = False
    length = len(pattern)
    for i in range(length - 2):
        chunk = pattern[i:i+3]
        if chunk == value:
            found = True
            return i
    if not found:
        print(f"[-] Value {value} is missing in the pattern!")
        return None


if __name__ == "__main__":
    print("=" * 40)
    print("Cyclic Pattern Generator")
    print("=" * 40)
    print("[*] Generating a pattern of 100 bytes...")
    pattern = pattern_generator(100)
    value = "Ab0"
    print(f"[*] Finding the value {value} in the pattern")
    position = position_finder(pattern, value)
    if position:
        print(f"[+] Value {value} found successfully!")
        print(f"[*] Position is at {position}")
