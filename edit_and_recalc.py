import glob


# from stackoverflow ref
def leftshift(int_in, shift_n, tot_bits):
    # returns an int.  take bin() to get  '0b10101'
    # bin(leftshift(int('10000000000000000000000000000000',2), 1, 32) )  ---> 0000...1
    return ((int_in << shift_n) % (1 << tot_bits)) | (int_in >> (tot_bits - shift_n))


def fix_checksum(bytarr):
    sum = 0 
    for i in range(len(bytarr)):
        # left shift for all idx
        sum = leftshift(sum, 1, 32) 
        sum += 0 if i in [12,13,14,15] else bytarr[i]

    bytarr[12:16] = sum.to_bytes(4, 'little')
    return bytarr


filename = glob.glob('*.d2s')[0]

# read .d2s char file bytes
with open(filename, 'rb') as f:
    bytarr = bytearray(f.read())  # f.read() is bytes object (not bytes array)

# save a backup of the .d2s char file
with open(filename + '.bak', 'wb') as f:
    f.write(bytarr)

# read patches
with open('patches.txt', 'r') as f:
    lines = f.read().splitlines()

# skip comments and blank lines and apply hex edits/patches
for line in [l for l in lines if l.strip() and l[0] != '#']:
    print(line)

    address = int(line.split(',')[0])
    hexstr_list = line.split(',')[1].strip().split()
    
    # edit bytesarray       # orig 0:2  int85, 170 -> (b'U\xaa') -> 55aa
    for i in range(len(hexstr_list)):
        bytarr[address + i] = int(hexstr_list[i], 16)

# write patched file with updated checksum
with open(filename, 'wb') as f:
    f.write(fix_checksum(bytarr))

print(f'd2s file {filename} saved successfully!')
