print("Hello")
def add(a, b):
    print("sum=",a+b)
add(2,3)

fact=1
num=5
for i in range(1,num+1):
    fact=fact*i
    print("factorial=",fact)
    
#num = int(input("Enter number: "))
#fact = 1
#for i in range(1, num + 1):
    #fact = fact * i
#print("Factorial =", fact)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
num = int(input("Enter number: "))
print("Factorial =", factorial(num))
