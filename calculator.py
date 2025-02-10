#A simple calculator program *(+,-,*,/) only

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y

print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

oper = int(input("Choose an operation: "))

if oper in (1,2,3,4):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if oper == 1:
        print("Answer:", add(num1, num2))
    elif oper == 2:
        print("Answer:", subtract(num1, num2))
    elif oper == 3:
        print("Answer:", divide(num1, num2))
    elif oper == 4:
        print("Answer:", multiply(num1, num2))
    else:
        print("Enter one of presented operations")
else:
    print("Choose one of presented operands")











