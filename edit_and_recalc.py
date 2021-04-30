
# refs
https://user.xmission.com/~trevin/DiabloIIv1.09_File_Format.shtml
https://www.geeksforgeeks.org/python-program-to-add-two-hexadecimal-numbers/
https://www.kite.com/python/answers/how-to-read-bytes-from-a-binary-file-in-python
https://stackoverflow.com/questions/5649407/hexadecimal-string-to-byte-array-in-python
https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_left_shift.html

https://wiki.python.org/moin/BitManipulation
https://stackoverflow.com/questions/63759207/circular-shift-of-a-bit-in-python-equivalent-of-fortrans-ishftc

https://github.com/krisives/d2s-format#checksum
calculating a 32-bit checksum:   (4bytes)
sum = (sum << 1) + data[i];


https://www.unf.edu/~cwinton/html/cop3601/s10/class.notes/assgn3-endian_format.pdf
# natural ordering (decimal 923) is big endian



a = 17

In [11]: hex(a)
Out[11]: '0x11'


aa = b'\x11'

In [18]: int.from_bytes(aa, 'little')
Out[18]: 17


aa = b'\x01'

bb = b'\x01'


int.from_bytes(aa, 'little') + int.from_bytes(bb, 'little')

# int() function with hexidecimal base
int('0x01', 16)
Out[35]: 1


# Calculating hexadecimal value using function
# aa should be a string.    b'\x01'  -->   '01'     bytesobj.hex() gives the str type
sum = hex(int(aa, 16) + int(bb, 16))


int(aa.hex(), 16) + int(bb.hex(), 16)

bytearray.fromhex(hex_string)


# bytearray using a hexidecimal string obj
arr = bytearray.fromhex('0001')

In [38]: arr
Out[38]: bytearray(b'\x00\x01')

In [39]: arr[0]  -->  0

In [40]: arr[1]  -->  1


bstring = '000102030A2233445566778899AA'
barray = bytearray.fromhex(bstring)


for b in barray:
    print(b)
    print(type(b))


bin(barray[0])



0b01  -->  int  type  1

In [71]: a = 0b01

In [72]: type(a)
Out[72]: int


# left shift bin(0b01 << 1)
Out[74]: '0b10'

# from stackoverflow ref above
def leftshift(int_in, shift_n, tot_bits):
    # returns an int.  take bin() to get  '0b10101'
    return ((int_in << shift_n) % (1 << tot_bits)) | (int_in >> (tot_bits - shift_n))

bin(leftshift(int('10000000000000000000000000000000',2), 1, 32) )  ---> 0000...1


### for the d2s checksum,  need to left rotate the sum (32bits) since doing 32, 33 left shifts will make the binary int 'overflow'
ff = 5
ff.to_bytes(4,'little').hex(' ')            # also  int.from_bytes()  is available
Out[139]: '05 00 00 00'

with open('testtt.d2s', 'rb') as f:
    for i in range(10):
        bread = f.read(1)  # 1st byte is  '55' a byte not int
        print(type(bread))
        print(bread.hex())


sum = 0
with open('testtt.d2s', 'rb') as f:
    btot = f.read()  # btot is bytes object (not bytes array)

    for i in range(len(btot)):
        if i in [12,13,14,15]:
            continue
        # print(hex(btot[i]))   # btot[0]  is 85, int

        sum = leftshift(sum, 1, 32)
        sum = sum + btot[i]
        
        

## read one byte at a time
sum = 0
idx = 0
with open('testtt.d2s', 'rb') as f:

    while b := f.read(1):
        if idx in [12,13,14,15]:
            b = b'\x00'

        sum = leftshift(sum, 1, 32)  # have to left shift for all idx
        sum = sum + int(b.hex(), 16)
        idx += 1


      
# function help for bytes.hex()
aa = bytes(2)
In [237]: aa.hex?
sep
    An optional single character or byte to separate hex bytes.  hex(' ')


sum.to_bytes(4, 'little').hex(' ')
Out[255]: '0f 1f 43 6c'                        ~~~~ matches the savefile!



0F 1F 43 6C    checksum




#### next:
add patches.txt to clear the cow level quest in act1

start offset: bytes to write
345+70  then 4th quest : 00 00   or   cain quest complete but cowking not killed

and once patches are written, calc the checksum and write that to offset12

