file=open("c:/byzs.txt")
#file.read(1)
print(len(file.read()))
print("Re-reading")
print(file.read())
print("Finished")
file.close()
