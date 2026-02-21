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

original_list=[1, 2, 3, 1, 2, 4, 'a', 'b', 'a', (1,2), (1,2)]
def remove_duplicates(x):
    unique_list=set(x)
    new_list=list(unique_list)
    return new_list
result=remove_duplicates(original_list)
print(result)
fact=1
num=6
for i in range(1,num+1):
    fact=fact*i
print("factorial=",fact)


#reverse string
s="hello"
def reverse_string(s):
    return s[::-1] 
print(reverse_string(s))

s="python"
rev=""
for ch in s:    #ch=p rev=p+"" rev=p ,ch=y rev= y+p rev=yp
    rev=ch+rev  
print(rev)

s="Himani"
rev="".join(reversed(s))
print(rev)