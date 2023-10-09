# Open a file as a binary file (to read byte by byte, not as a text file)
infile = open('greenbox.bmp', 'rb')
data = []
# Read one byte from file and store it in variable byte
byte = infile.read(1)

while byte:
    # To convert byte to an integer in range 0-255 you need to use int.from_bytes()
    data.append(int.from_bytes(byte, 'little'))
    byte = infile.read(1)

# Now the whole file should be read into data.
print(data)

# Change 3000 bytes in the middle to 127
for i in range(9000, 12000):
    data[i] = 127

infile.close()

# Open an output file for writing (as a binary file)
outfile = open('output.bmp', 'wb')

# You can now write the array of integers, interpreted as bytes to your new file.
outfile.write(bytearray(data))
outfile.close()