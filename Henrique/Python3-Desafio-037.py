# Challenge 037
# Numbering System Converter
print("Numbering System Converter")
decimal = int(input("Please, enter the decimal number"))
binary = []
while decimal != 0: 
    binary.append(decimal % 2)
    print("binary: ", binary)
    decimal = (decimal // 2)
    print("decimal: ", decimal)

print("binary: ", binary)
binary.reverse()
binaryReversed = binary

print("binary: ", binary)
binaryConverted = 0
while  int(binaryReversed.count(0) + binaryReversed.count(1)) != 0:
    binaryConverted = str(binaryConverted) + str(binaryReversed.pop())

print("binary: ", binaryReversed)

print("binaryConverted: ", binaryConverted)
