#program to computer x^y without using math functions 

def computePower(x, y):

    #defaukt total is 1

    result = 1

    while (y > 0):

        #if y is even

        if (y % 2 == 0):
            x = x*x
            y>>= 1

        else:

            result = result * x
            y = y - 1

    return result

x = int(input("Enter the x for x^y: "))
y = int(input("Enter the y for x^y: "))
print ("Total : ", computePower(x, y))