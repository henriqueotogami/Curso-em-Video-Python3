# Challenge 037
# Numbering System Converter
print("Numbering System Converter")
decimal = int(input("Please, enter the decimal number"))
decimalInt = decimal
binary = []
while decimalInt != 0: 
    binary.append(decimalInt % 2)
    decimalInt = (decimalInt // 2)

print(binary)

binaryConverted = ""
for index in binary.__reversed__():
    binaryConverted = str(binaryConverted) + str(binary.pop(index-1))

print("binaryConverted: ", binaryConverted)
# print(type(binaryConverted))

hexadecimalList = [("0", "0000"), ("1", "0001"), ("2", "0010"), ("3", "0011"), ("4", "0100"), ("5", "0101"), ("6", "0110"), ("7", "0111"), ("8", "1000"), ("9", "1001"), ("A", "1010"), ("B", "1011"), ("C","1100"), ("D", "1101"), ("E", "1110"), ("F","1111")]

# print(type(hexadecimalList))
# print(len(hexadecimalList))
quantDigits = len(binaryConverted)
quantBundles = (quantDigits%4)

# print(quantDigits)
# print(quantBundles)
# print(type(quantBundles))

while quantBundles != 0:
    binaryConverted = "0" + binaryConverted
    quantDigits = len(binaryConverted)
    quantBundles = (quantDigits%4)

binaryConverted = binaryConverted[::-1]
print(binaryConverted)
print(quantDigits)
quantBundles = int(quantDigits/4)
print(quantBundles)

binaryList2 = []
index = 0
index2 = 1
while quantBundles != 0:
    binaryList2.append(binaryConverted[index*4:index2*4])
    quantBundles -= 1
    index += 1
    index2 += 2

print(binaryList2)


newlist = [x for x in binaryList2[x] if binaryList2[x] in hexadecimalList]

print("newlist:{}",newlist)


