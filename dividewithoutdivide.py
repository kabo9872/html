# program to divide 2 numbers without using division operator

def divide(OurDividend, OurDivisor):
    # check if divisor is -ve or +ve
    sign = (-1 if ((OurDividend < 0) ^ (OurDivisor < 0)) else 1)

    # make both positive
    OurDividend = abs(OurDividend)
    OurDivisor = abs(OurDivisor)

    quotientNumber = 0
    tempNumber = 0

    # go from 31 to 0 and accumulate all valid bits
    for i in range(31, -1, -1):
        if (tempNumber + (OurDivisor << i) <= OurDividend):
            tempNumber += OurDivisor << i
            quotientNumber |= 1 << i

    # assuming the sign value is -1, negate the quotiant value
    if sign == -1:
        quotientNumber = -quotientNumber
    return quotientNumber

a = int(input("enter a for a/b:"))
b = int(input("enter b for a/b:"))
print("result of",a,"/",b,"is",divide(a,b))