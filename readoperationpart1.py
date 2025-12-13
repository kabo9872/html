file = open ('codingal.txt','r')
print(file.read())
file.close()


file = open ('codingal.txt','r')
print(" read in parts \n")
print(file.read(8))
file.close()


file = open ('codingal.txt','a')
file.write("Hi! I am kabo and I am 14 years old.")
file.close()