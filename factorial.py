def recur_factorial(n):

    if n == 1:
        return n
    else:
        return n * recur_factorial(n-1)
    

num = int(input("enter a number"))

if num<0:
    print("sorry, factorial does not exist for negetive numbers")
elif num == 0:
    print("factorial 0 is 1")
else:
    print("The factorial of", 5 ,"is", recur_factorial(5))