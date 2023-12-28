'''ByteArray Function is changeable.but bytearray Function
 is range also same on byte Function.(0-255)'''

listItem = [5,8,9,6,7,6,8]

convertByteArray = bytearray(listItem)

convertByteArray[2] = 52



print(type(convertByteArray))


