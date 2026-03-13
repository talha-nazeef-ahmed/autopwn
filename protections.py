#!/usr/bin/env python3

import subprocess


def check_protections(binary_path):
    result = subprocess.run(
        ["checksec", f"--file=./{binary_path}"],
        capture_output=True,
        timeout=10
    )
    output = result.stdout.decode()
    protection = {
        "Canary": True,
        "NX": True,
        "PIE": True,
        "ASLR": True
    }
    for i in output.split("\n"):
        if "No canary found" in i:
            protection["Canary"] = False
        if "NX disabled" in i:
            protection["NX"] = False
        if "No PIE" in i:
            protection["PIE"] = False
    f = open("/proc/sys/kernel/randomize_va_space", "r")
    aslr = f.read().strip()
    f.close()
    if int(aslr) == 0:
        protection["ASLR"] = False
    return protection


def print_protections(protection):
    print("[*] Binary Protections:")
    for key, value in protection.items():
        if value:
            print(f"{key}:\t Enabled")
        else:
            print(f"{key}:\t Disabled")


def decide_strategy(protection):
    print("[*] Choosing the path...")
    if not protection["NX"]:
        print("[+] Path: Direct Shellcode on the stack is possible")
        if not protection["ASLR"] and not protection["PIE"]:
            print(
                "[->] Binary addresses are fixed, we could use jmp esp from the binary itself")
        else:
            print("[->] Need to leak the address first before direct shellcode")
    else:
        print("[+] Path: Direct shellcode is not possible, need ret2libc or ROP")
        if protection["Canary"]:
            print(
                "[->] Canary is on, need to leak the canary first before ret2libc or ROP")


if __name__ == "__main__":
    result = check_protections("binaries/vuln1")
    print_protections(result)
    decide_strategy(result)
