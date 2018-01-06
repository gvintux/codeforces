import re
import string


def convert_address(address):
    result_address = ""
    abc_len = 26
    if re.search("R\d+C\d+", address) is not None:
        row, col = map(int, address[1:].split('C'))
        while col > abc_len:
            result_address += string.ascii_uppercase[col // abc_len - 1]
            col = col % abc_len
        result_address += string.ascii_uppercase[col - 1] + str(row)
    else:
        for idx, c in enumerate(address):
            if c.isdigit():
                break
        row = address[idx:]
        col = address[:idx]
        col_num = 0
        result_address += 'R'
        for idx in range(0, len(col)):
            col_num += (string.ascii_uppercase.find(col[-1]) + 1) * 26 ** idx
            col = col[:-1]
        result_address += row + 'C' + str(col_num)
    return result_address


addresses = list()
n = input()
n = int(n)
for i in range(0, n):
    addresses.append(input())
for i in range(0, n):
    print(convert_address(addresses[i]))
