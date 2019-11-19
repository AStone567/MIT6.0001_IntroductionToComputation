#Finger Excercise 3.4 - Few Words about using Float:
#What is the decimal equivalent of the binary number 10011?

binary = '10011'
total = 0
bits = len(binary) - 1

for x in binary:
    if x == '1':
        total += int(x) * (2**bits)
    bits -= 1

print(total)


#OR

#Using the enumerate function
# binary = '10011'
# total = 0
# for i, b in enumerate(reversed(binary)):
#     if b == 1:
#         total += 2**(i)
#     print(total)
