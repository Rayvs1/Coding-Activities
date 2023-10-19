def getNumber(prompt):
    x=int(input(prompt))
    return x

def getSum(fN, sN):
    s=fN + sN
    return s

def displayresult(result):
    print(result)

a = getNumber("Enter First Number: ")
b = getNumber("Enter the Second Number: ")
c = getSum(a, b)

displayresult("sum"+str(c))

displayresult(str(getSum(getNumber("Num1: "),getNumber("Num2: "))))
                         
    
    
