number = int(input("number to check :"))
print("number to check : ", number)

if number>50:

    if number%2 == 0:
        print("the number is greater than 50 and is even")

    else:
        print("the number is greater than 50 but is odd")

else:
    print("the number is less than 50")