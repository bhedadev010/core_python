#no arguement no return value

def printLine():
    print("*"*50)

printLine()
print("Welcome to udf")
printLine()

#with arguements and no return value

def add(a,b):
    print("Addition :",a+b)

add(10,20)
printLine()

#with arguements and with return value

def subtract(a,b):
    return a-b

#ans=suntract(20,10)
#if you want to use variable value in multiple places use a variable, otherwise directly place in print()

print("Subtraction of a and b is :",subtract(20,10))
printLine()



#4th type no arguements with return value is not used because it is not useful in any scenario