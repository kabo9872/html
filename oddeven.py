#program to check if the entered number is odd or even using bitwise operator
#return true if the number is even, else odd
def isEvenOdd(n):
#XOR with 1 = n+1
    if (n ^ 1 == n + 1):
        return True;
    else:
        return False;

number = int(input("Enter a number: "))

if (isEvenOdd(number)):
    print(number, "is an even number")

else:
    print(number, "is an odd number")

    