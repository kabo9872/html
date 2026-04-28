#program to check if the number is the power of 4

def power4(number):

    count = 0

    #if only 1 set bit exists

    if (number & (~(number & (number - 1)))):

        #count 0 bit befor set bit

        while (number > 1):
            number = number >> 1
            count += 1

            #if count is even return true else false

            if (count % 2 ==0):
                return True
            else:
                return False

number = int(input("Enter the number: "))

if (power4(number)):
    print("\nThe number is a power of 4")
else:
    print("\nThe number is not a power of 4")