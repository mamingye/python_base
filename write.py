#file=open("c:/write.txt","w")
#file.write("this has been written to a file by python")
#file.close()

file=open("c:/write.txt")

print(file.read())
file.close()

#file=open("c:/write.txt","w")
#file.close()
#file=open("c:/write.txt")
#print(file.read())

with open("c:/write.txt") as f:
        print(f.read(1))