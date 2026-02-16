#!/usr/bin/env python3
import os
from fuzzer import run_binary, check_crash
from pattern import pattern_generator, position_finder
from core_reader import read_eip, eip_to_pattern

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
    pattern = pattern_generator(size + 20)
    print(f"[*] Generated cyclic pattern ({size + 20} bytes)")
    payload = pattern.encode()
    check = run_binary(payload)
    if check:
        print(f"[+] Program crashed with cyclic pattern!")
        print("\n[Phase 3] Finding EIP")
        print("-" * 40)
        binary_path = f"{os.getcwd()}/binaries/vuln1"
        eip = read_eip(binary_path, pattern)
        if eip is None:
            print("[-] Could not read EIP!")
        else:
            print(f"[+] EIP: {eip}")
            pattern_from_eip = eip_to_pattern(eip)
            print(f"[+] Pattern value: {pattern_from_eip}")
            offset = position_finder(pattern, pattern_from_eip)
            if offset is not None:
                print(f"\n{'=' * 50}")
                print(f"[+] OFFSET TO RETURN ADDRESS: {offset} bytes")
                print(f"{'=' * 50}")
    else:
        print("[-] Program didn't crash with cyclic pattern")
