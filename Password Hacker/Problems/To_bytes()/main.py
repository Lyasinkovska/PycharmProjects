n = int(input())
print(sum(n.to_bytes(2, byteorder="little")))