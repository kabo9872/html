file = open ('codingal.txt','r')
print("reading first line..")
print(file.readline())
file.close()


file = open ('codingal.txt','r')
print("reading multiple lines..")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


file = open ('codingal.txt','r')
print("Looping through the lines")

for line in file:
    print(line)
file.close()