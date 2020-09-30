message = input().encode()
integer = sum(int(input()).to_bytes(2, byteorder="little"))
print(''.join([chr(elem+integer) for elem in message]))