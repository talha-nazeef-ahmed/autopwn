#!/usr/bin/env python3
import subprocess


def read_eip(binary_path, payload):
    result = subprocess.run(
        ["gdb", binary_path, "-batch", "-ex", "run", "-ex", "info registers eip"],
        input=payload.encode() if isinstance(payload, str) else payload,
        capture_output=True,
        timeout=10
    )
    output = result.stdout.decode()
    for i in output.split("\n"):
        if "eip" in i:
            parts = i.split()
            for j in parts:
                if j.startswith("0x"):
                    return j
    return None


def eip_to_pattern(eip):
    hex_str = eip.replace("0x", "")
    char_list = []
    for i in range(0, len(hex_str), 2):
        chunk = hex_str[i:i+2]
        ascii_val = int(chunk, 16)
        char = chr(ascii_val)
        char_list.append(char)
    char_list.reverse()
    pattern = "".join(char_list)
    return pattern


if __name__ == "__main__":
    print("=" * 40)
    print("   Core Reader Test (No Core Dumps!)")
    print("=" * 40)

    from pattern import pattern_generator, position_finder

    pattern = pattern_generator(100)
    print(f"[*] Pattern: {pattern[:50]}...")

    eip = read_eip('./binaries/vuln1', pattern)
    print(f"[+] EIP: {eip}")

    if eip:
        value = eip_to_pattern(eip)
        print(f"[+] Pattern value: {value}")
        offset = position_finder(pattern, value)
        print(f"[+] Offset: {offset}")
