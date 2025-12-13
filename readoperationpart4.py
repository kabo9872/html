fileorigional = open('codingal.txt','r')

fileupdated = open('CodingalUpdated.txt','w')

cont = fileorigional.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if(i % 2 != 0):
        fileupdated.write(cont[i-1])
    else:
        pass

fileupdated.close()


fileupdated = open('CodingalUpdated.txt','r')

cont1 = fileupdated.read()

print(cont1)

fileorigional.close()
fileupdated.close()