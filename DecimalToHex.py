#Using python 3
#base10 to base16 converter

hexNumberArray =[]
base16 = {10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}


def decimalToHex(decNumber):
    remainder = 5
    while remainder >= 1:
        remainder=int(decNumber % 16)
        decNumber /= 16
        if remainder > 9:
            hexNum=base16[remainder]
            hexNumberArray.append(hexNum)
        elif remainder == 0:
            hexNumberArray.append(int(decNumber))
        else:
            hexNumberArray.append(remainder)
    hexNumberArray.reverse()
    result = ''.join(map(str,hexNumberArray))
    print("0x"+result)











decNumber = int(input("Enter base10 decimal number:"))

decimalToHex(decNumber)
