def myfunc2(x,y,z=10):
    sum = x + y + z
    print("Sum = " +str(sum))


    
def myfunction1():
    print("Inside Function 1")
    return 10



x = myfunction1()
print(x)

myfunc2(10,20,30)
myfunc2(y=20, z=30, x=10)
myfunc2(10,20)
print("sum = " +str(y))
