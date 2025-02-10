#A Program should allow input in console and show if number is prime or not
import math

def prime(x):
    if x < 2:
        return False
    for n in range(2, int(math.sqrt(x)) + 1 ):
        if x % n == 0:
            return False
    return True

value = int(input("Enter suspect number: "))

if prime(value):
    print(value, "is a prime number.")
else:
    print(value, "in not a prime number.")


