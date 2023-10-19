import myModule as x

a = x.getNumber("Enter first number: ")
b = x.getNumber("Enter second number: ")
c = x.getNumber("Enter third number: ")
d = x.getNumber("Enter fourth number: ")
e = x.getNumber("Enter fifth number: ")
f = x.getSoFNM(a,b,c,d,e)
g = x.getAoFN(f)
x.displayresult("Average = "+str(g))
