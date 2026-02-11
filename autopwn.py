#!/usr/bin/env python3

from fuzzer import run_binary, check_crash
from pattern import pattern_generator, position_finder

print("=" * 60)
print("         Autopwn - Binary Exploitation Tool          ")
print("         by Talha Nazeef Ahmed                       ")
print("=" * 60)
print("\n[Phase 1] Fuzzing")
print("-" * 40)
size = check_crash()
if size > -1:
    print("\n[Phase 2] Offset Discovery")
    print("-" * 40)
    pattern = pattern_generator(size)
    print(f"[*] Generated cyclic pattern ({size} bytes)")
    payload = pattern.encode()
    check = run_binary(payload)
    if check:
        print(f"[+] Program crashed with cyclic pattern!")
        print(f"\n[*] Pattern sent: {pattern}")
    else:
        print("[-] Program didn't crash with cyclic pattern, debugging the issue...")
