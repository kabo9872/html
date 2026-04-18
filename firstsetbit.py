num = int(input("Enter a number: "))

rightmost_set_bit = num & -num

print("rightmost_set_bit: ", rightmost_set_bit)