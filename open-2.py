file=open("c:/byzs.txt","r")
for i in range(20):
    print(file.read(4))
file.close()