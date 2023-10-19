'''a=["HI", 20, 3.14, "X"]
print(a)
a.pop()
print(a)
a.remove(20)
print(a)
a[1]=100
print(a)


a={'key1':3.1416, 'key2': "ola mundo"}
print(a['key2'])
a['key2']="hello world"
print(a['key2'])
a['key3']="sevvi"
print(a)
#a.clear()
a.pop('key3')
print(a)


x=0
myStr=""
while x<=100:
    if x%3==0:
        myStr=myStr+str(x)+ " "
    x=x+1
print(myStr)


ctr=10
while(ctr>=1):
    print(ctr)
    ctr=ctr-1

n=1
while n <5:
    print("HELLO WORLD")
    n=n+1
'''    
    
x=0
while x<=20:
    x+=1
    if x%3==0 or x%4==0:
        continue
    else:
        print(x)
   
    
    
