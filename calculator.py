def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a/b
while True:
    print("****Calculator****")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '5':
        print("Exiting the calculator.")
        break
    
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    
    if choice == '1':
        print("Result:", add(a,b))
    elif choice == '2':
        print("Result:", subtract(a,b))
    elif choice == '3':
        print("Result:", multiply(a,b))
    elif choice == '4':
        print("Result:", divide(a,b))
    else:
        print("Invalid Choice.")
    