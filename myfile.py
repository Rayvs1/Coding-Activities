myfile=open("Type.txt","a+")
myfile.write("Hello")
myfile.write("hi-")
myfile.write("Ola")

myfile.close()
myfile2=open("Type.txt", "r")
value=myfile2.read()
print(value)
myfile2.close()


