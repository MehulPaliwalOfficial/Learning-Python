# Converting between number systems:
# print(int("10101", 2))  # Convert binary to decimal
# print(int("a5b", 16))  # Convert hexadecimal to decimal
# print(bin(1659))  # Convert decimal to binary
# print(oct(1659))  # Convert decimal to octal
# print(hex(1659))  # Convert decimal to hexadecimal

# Binary is a base 2 number system that uses only two digits, 0 and 1. Each digit in a binary number is called a bit. Binary numbers are used in computers and digital systems to represent data and perform calculations.
# print(bin(17))
# print(bin(37))
# print(bin(100))
# print(bin(255))
# print(bin(1024))
# print(bin(2048))
# print(bin(4096))

# Octal is a base 8 number system that uses digits from 0 to 7. Each digit in an octal number represents three bits in binary. Octal numbers are often used in computer programming and digital systems as a shorthand representation of binary numbers.
# print(oct(17))
# print(oct(37))
# print(oct(100))
# print(oct(255))
# print(oct(1024))
# print(oct(2048))
# print(oct(4096))

# Hexadecimal is a base 16 number system that uses digits from 0 to 9 and letters A to F (or a to f) to represent values. Each digit in a hexadecimal number represents four bits in binary. Hexadecimal numbers are commonly used in computer programming, digital systems, and memory addressing.
# print(hex(17))
# print(hex(37))
# print(hex(100))
# print(hex(255))
# print(hex(1024))
# print(hex(2048))
# print(hex(4096))

# ZOR (Zero One Representation) is a binary representation of numbers where each digit is represented by either 0 or 1. It is commonly used in computer systems and digital electronics to represent data and perform calculations.
# print(234^234)  # 1,1 = 0
# print(234^123)  # 1,0 = 1
# print(123^234)  # 0,1 = 1
# print(123^123)  # 0,0 = 0
# print(234^0)    # 1,0 = 1

# Bitwise operations are operations that directly manipulate individual bits of binary numbers. They are commonly used in computer programming and digital systems for tasks such as data manipulation, encryption, and optimization.
# print(bin(3))
# print(bin(3 << 1))  # Left shift operation shifts the bits of a binary number to the left by a specified number of positions. It effectively multiplies the number by 2 for each position shifted. For example, shifting the binary representation of 3 (which is 11 in binary) to the left by 1 position results in 6 (which is 110 in binary).
# print(bin(3 << 2))
# print(bin(3 >> 1))  # Right shift operation shifts the bits of a binary number to the right by a specified number of positions. It effectively divides the number by 2 for each position shifted. For example, shifting the binary representation of 3 (which is 11 in binary) to the right by 1 position results in 1 (which is 1 in binary).
# print(bin(3 >> 2))
# print(bin(3 & 1))  # Bitwise AND operation compares each bit of two binary numbers and returns a new binary number where each bit is set to 1 if both corresponding bits are 1, and 0 otherwise. For example, performing a bitwise AND operation between the binary representations of 3 (which is 11 in binary) and 1 (which is 01 in binary) results in 1 (which is 01 in binary).
# print(bin(3 & 2))
# print(bin(3 and 1))
# print(bin(3 | 1))  # Bitwise OR operation compares each bit of two binary numbers and returns a new binary number where each bit is set to 1 if at least one of the corresponding bits is 1, and 0 otherwise. For example, performing a bitwise OR operation between the binary representations of 3 (which is 11 in binary) and 1 (which is 01 in binary) results in 3 (which is 11 in binary).
# print(bin(3 | 2))
# print(bin(3 or 1))

print(7>>1)
print(16&1)