#program to find the number f zero bits and one bits represented in the number

#functions take our number as input

def numberOfBits(n):

    ones=0
    zeros=0

    #while our number is greater than 0 we will check the last bit and right shift

    while(n):

        if(n%1==1):
            ones+=1

        else:

            zeros+=1

            #right shift the number and remove the last bit that we checked above

            n>>=1
            print("\n\nOnes =",ones,"\nZeros =",zeros)


number = int(input("Enter a number: "))
numberOfBits(number)




