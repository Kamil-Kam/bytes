import struct

text = b'Hello World'
print(text)
# b'Hello World'

text_2 = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'
print(text_2)
# b'Hello World'

print(text == text_2)
True

def transform_1(text):
    return [x for x in text]
print(transform_1(text))
# [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]

def transform_2(text):
    return [hex(x) for x in text]
print(transform_2(text))
# ['0x48', '0x65', '0x6c', '0x6c', '0x6f', '0x20', '0x57', '0x6f', '0x72', '0x6c', '0x64']
      
def transform_3(text):
    return [int(hex(x), 16) for x in text]
print(transform_3(text))
# [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]

def transform_4(text):
    return [bytes.fromhex(hex(x)[2:]) for x in text]
print(transform_4(text))
# [b'H', b'e', b'l', b'l', b'o', b' ', b'W', b'o', b'r', b'l', b'd']

print('=' * 100)

numbers = 123

print(transform_1(b'123'))
# [49, 50, 51]

# numbers must be in range -128, 127
def transform_5(numbers):
    return struct.pack('b', numbers)
print(transform_5(numbers))
# b'{'

# numbers must be in range 0, 255
def transform_6(numbers):
    return bytes([numbers])
print(transform_6(numbers))
# b'{'

def transform_7(numbers):
    packed = transform_6(numbers)
    return struct.unpack('b', packed)
print(transform_7(numbers))
# (123,)

print('=' * 100)

print(hex(numbers))
# 0x7b

print(bin(numbers))
# 0b1111011

binary_data = "01010100 01100101 01110011 01110100"

bytes_data = bytes([int(byte, 2) for byte in binary_data.split()])
print(bytes_data)
# b'Test'

