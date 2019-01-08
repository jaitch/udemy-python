import math
def sum(x, y):
    sum = x + y
    return sum
def difference(x, y):
    diff = x - y
    return diff
def product(x, y):
    product = x * y
    return product
def quotient(x, y):
    quotient = x / y
    return quotient
def remainder(x, y):
    remainder = x % y
    return remainder
def exponent(x, y):
    exponent = x ** y
    return exponent

def main():
    print("a = addition, s = subtraction, m = multiplication, d = division, r = remainder, e = exponent")
    oper = input("What operation would you like to perform? (a, s, m, d, r, e) ")
    num1 = input("What is the first number? ")
    num2 = input("What is the second number? ")
    float(num1)
    float(num2)
    if oper == "a":
        answer = sum(float(num1), float(num2))
        print("The sum is " + str(answer))
    if oper == 's':
        answer = difference(float(num1), float(num2))
        print("The difference is " + str(answer))
    if oper == "m":
        answer = product(float(num1), float(num2))
        print("The product is " + str(answer))
    if oper == "d":
        answer = quotient(float(num1), float(num2))
        print("The quotient is " + str(answer))
    if oper == "r":
        answer = remainder(float(num1), float(num2))
        print("The remainder is " + str(answer))
    if oper == "e":
        answer = exponent(float(num1), float(num2))
        print("The answer is " + str(answer))
main()
