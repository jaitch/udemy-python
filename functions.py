name = "Janice"
num1 = 3
num2 = 7
num3 = 50


def stringAdder(word1, word2):
    print((word1) + " + " + (word2) + "= " + (word1) + (word2))


stringAdder("dog", "cat")

def nameNamer(nombre):
    print (nombre)

nameNamer(name)

def numberMultiplier(num1, num2):
    product = num1 * num2
    return product

product = numberMultiplier(num1, num2)
print (product)

def numberTester(number):
    if number > 50:
        print ("your number is greater than 50")
    elif number == 50:
        print ("your number IS 50")
    else: print ("your number is less than 50")
numberTester(num3)
