#program to find the element not making a pair

#function to calculate the number that is odd occurring

def OddOccurring(arr):

    #initial result

    res = 0

    #transverse the array
    for element in arr:
        #XOR with the result
        res = res ^ element

    return res

#anitialize our array

arr = []

#take array size as input

n = int(input("enter the size of the array:"))

#take array elements input

while(n):

    num= int(input("enter the number:"))
    arr.append(num)
    n -= 1

print("\n\n Odd occuring number is:", OddOccurring(arr))