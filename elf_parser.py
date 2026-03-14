#!/usr/bin/env python3

def parse_elf(binary_path):
    f = open(binary_path, "rb")
    data = f.read(32)
    f.close()
    if data[0:4] == b"\x7fELF":
        entry_point = 0
        return_data = {
            "arch": "",
            "endian": "",
            "entry": ""
        }
        if data[4] == 1:
            return_data["arch"] = "32-bit"
        else:
            return_data["arch"] = "64-bit"
        if data[5] == 1:
            return_data["endian"] = "little"
        else:
            return_data["endian"] = "big"
        if return_data["arch"] == "32-bit":
            entry_point = int.from_bytes(
                data[24:28], byteorder=f"{return_data['endian']}")
        else:
            entry_point = int.from_bytes(
                data[24:32], byteorder=f"{return_data['endian']}")
        hex_num = hex(entry_point)
        return_data["entry"] = hex_num
        return return_data

    else:
        print("Error! File type is not an elf binary")
        return None


if __name__ == "__main__":
    test = parse_elf("binaries/vuln1")
    print(test)
