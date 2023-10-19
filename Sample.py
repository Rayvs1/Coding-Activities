import os

if(not(os.path.exists("users.txt"))):
    myfile=open("users.txt","a")
    myfile.close()

def addUser():
    username=input("Input Usernamer: ")
    password=input("Input Password: ")
    value=username+","+password+"-"
    myfile=open("user.txt","a")
    myfile.write(value)
    myfile.close()

def viewUsers():
    myfile=open("users.txt", "r")
    contents=myfile.reaf()
    users=contents.split("-")
    print("List of Users")
    for x in range(len(users)-1):
        splitx=users(x).split(",")
        uname=splitx(0)
        password=splitx(1)
        print(uname+"/"+password)
        
        
    

print("[1] Add user")
print("[2] View Users")
print("[x] exit")

choice = input("Please select an option")
if(choice=="1"):
    addUser()
elif(choice=="2"):
    viewUser()
elif(choice=="x"):
    print("goodbye")
else:
    print("Invalid choice")
