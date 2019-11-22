'''
given 2 numbers (traditionally 3 and 5), for the first 1000 numbers if the number is divisible by the first number print fizz,
if its divisible by the second number print buzz and if its both print fizzbuz
'''

def fizzBuzz(firstNumber,secondNumber):
    for x in range(1000):
        if x % firstNumber == 0 and x % secondNumber == 0:
            print("fizzbuzz")
        elif x % firstNumber == 0:
            print("fizz")
        elif x % secondNumber == 0:
            print("buzz")
        else:
            print(x)

fizzBuzz(3,5)
