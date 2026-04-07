#Program to find the hcf and gcd

#enter 2 numbers
numberLargest=int(input("Enter the largest number: "))
numberSmallest=int(input("Enter the smallest number: "))

#Using eucliden algorythms to find the hcf and gcd
while (numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

    print("HCF is: ", numberLargest)