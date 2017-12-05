import string
import itertools

def crc_message(msg):
    crc = 0 ^ 0xFFFFFFFF
    for i in msg:
        crc = crc32(ord(i), crc, )
    return crc ^ 0xFFFFFFFF


def crc32(byte, crc):
    crc ^= byte
    for k in range(0, 8):
        if crc & 1:
            crc = (crc >> 1) ^ crc_polynom
        else:
            crc = crc >> 1
    return crc

def crc_with_table(msg, table):
    pass

def brute(target_hash):
    baseChars = string.ascii_letters + string.digits
    for i in itertools.product(baseChars, baseChars, baseChars, baseChars):
        joined = ''.join(i)
        print("Testing %s" % joined)
        if crc_message(joined) == target_hash:
            return joined

def gen_table(polynom):
    table = []
    for i in range(0, 256):
        entry = i
        for j in range(8, 0, -1):
            if entry & 1:
               entry = (entry >> 1) ^ polynom
            else:
                entry >>=1
        table.append(entry)
    
    return table

def patch(wanted):
    w = wanted ^ 0xFFFFFFFF
    table = []
    for i in range(0, len(crc_table)):
        table.append(crc_table[i])

    table.sort()
    message = []
    r = []
    width = 4
    hash = 0xFFFFFFFF
    for p in range(0, width):
        message.append((hash & (256**(p+1)-1)) >> (8 * p))
    for p in range(0, width):
        message.append((w & (256**(p+1)-1)) >> (8 * p))
    for p in range(width - 1, -1, -1):
        o = table[message[p+width]]
        for q in range(0,width):
            v = (o & (256**(q+1)-1)) >> (8 * q)
            message[p+q+1] = message[p+q+1] ^ v
        message[p] = message[p] ^ crc_table.index(o)
    for p in range(0, width):
        r += chr(message[p])
    return r

keys = [
    0x69355f71,
    0xc2c8c11c,
    0xdf45873c,
    0x9d26aaff,
    0xb1b827f4,
    0x97d1acf4
]

crc_polynom = 0xedb88320
crc_table = gen_table(crc_polynom)

for key in keys:
    #print(brute(key))
    print(''.join(patch(key)))