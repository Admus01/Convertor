import argparse
import math

parser = argparse.ArgumentParser(description="convert values")

parser.add_argument("--converting_value", "-cv", type=str, required=True)

parser.add_argument("--from_system", "-fs", type=str, required=True)

parser.add_argument("--to_system", "-ts", type=str, required=True)

args = parser.parse_args()

length = len(args.converting_value) - 1
result = 0
power = 0


if args.from_system == args.to_system:
    print("You're converting among same systems dummy")


if args.from_system.lower() == "hex" and args.to_system.lower() == "dec":
    while length >= 0:
        if args.converting_value[length].lower() == ("a" or "b" or "c" or "d" or "e" or "f"):
            value = ord(args.converting_value[length].lower()) - 87

        else:   
            value = int(args.converting_value[length])

        result += value * 16 ** power
        length -= 1
        power += 1
    
    print(result)


if args.from_system.lower() == "bin" and args.to_system.lower() == "dec":
    while length >= 0:
        result += int(args.converting_value[length]) * 2 ** power
        length -= 1
        power += 1
    
    print(result)


if args.from_system.lower() == "oct" and args.to_system.lower() == "dec":
    while length >= 0:
        result += int(args.converting_value[length]) * 8 ** power
        length -= 1
        power += 1
    
    print(result)


if args.from_system.lower() == "dec" and args.to_system.lower() == "hex":
    reversedStringResult = ""
    stringResult = ""

    tempResult = int(args.converting_value)

    while tempResult != 0:
        result = tempResult % 16
        if result >= 10:
            reversedStringResult += chr(result + 55)
        else:
            reversedStringResult += str(result)
        tempResult = math.floor(tempResult / 16)

    length = len(reversedStringResult) - 1

    while length >= 0:
        stringResult += reversedStringResult[length]
        length -= 1

    print(stringResult)


if args.from_system.lower() == "dec" and args.to_system.lower() == "bin":
    reversedStringResult = ""
    stringResult = ""

    tempResult = int(args.converting_value)

    while tempResult != 0:
        result = tempResult % 2
        if result >= 10:
            reversedStringResult += chr(result + 55)
        else:
            reversedStringResult += str(result)
        tempResult = math.floor(tempResult / 2)

    length = len(reversedStringResult) - 1

    while length >= 0:
        stringResult += reversedStringResult[length]
        length -= 1

    print(stringResult)


if args.from_system.lower() == "dec" and args.to_system.lower() == "oct":
    reversedStringResult = ""
    stringResult = ""

    tempResult = int(args.converting_value)

    while tempResult != 0:
        result = tempResult % 8
        if result >= 10:
            reversedStringResult += chr(result + 55)
        else:
            reversedStringResult += str(result)
        tempResult = math.floor(tempResult / 8)

    length = len(reversedStringResult) - 1

    while length >= 0:
        stringResult += reversedStringResult[length]
        length -= 1

    print(stringResult)


if args.from_system.lower() == "bin" and args.to_system.lower() == "hex":
    reversedStringResult = ""
    stringResult = ""
    tempResult = 0
    if length <= 4:
        i = 1
    else:
        i = math.ceil(length / 4)
    
    while i > 0:
        tempResult = 0
        power = 0
        while True:
            tempResult += int(args.converting_value[length]) * 2 ** power
            if length % 4 == 0:
                break
            length -= 1
            power += 1
        i -= 1
        length -= 1

        if tempResult > 9:
            reversedStringResult += chr(tempResult + 55)
        else:
            reversedStringResult += str(tempResult)
    
    length = len(reversedStringResult) - 1

    while length >= 0:
        stringResult += reversedStringResult[length]
        length -= 1

    print(stringResult)
    
