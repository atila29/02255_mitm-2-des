import des
from des import DesKey

key0 = DesKey(b"000000000000000000000000")
key1 = DesKey(b"111111111111111111111111")

key0.is_single()

encMSG0 = key0.encrypt(b"blablabla", padding=True)
encMSG1 = key1.encrypt(encMSG0)

def pad(key, size):
    padding = "".join(["0" for i in range(0, size - len(key))])
    paddedKey = padding + key
    evenBytesPaddedKey = []
    for i in range(0,8):
        for j in range(0,7):
            evenBytesPaddedKey.append(paddedKey[i * 7 + j])
        evenBytesPaddedKey.append(str(evenBytesPaddedKey[i * 8: i * 8 + 7].count('1') % 2))

    evenBytesPaddedKey = "".join(evenBytesPaddedKey)
    evenBytesPaddedKey = int(evenBytesPaddedKey, 2)
    evenBytesPaddedKey = evenBytesPaddedKey.to_bytes(size // 8, byteorder='big')
    return evenBytesPaddedKey

keys = range(0, 2 ** 20)
print(keys[3])
print("{0:b}".format(keys[3]))
print(pad("1011", 64))
print("{0:b}".format(23))
"""
keysInBinary = [pad("{0:b}".format(k), 64) for k in keys]
print(keysInBinary[0])
print(keysInBinary[1])
print(keysInBinary[10])
print(keysInBinary[-1])
"""
key0 = DesKey(pad("11101000011100010100", 64))
key1 = DesKey(pad("10001101111111111111", 64))
