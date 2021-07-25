name = input("what is your name ?")

print(f"wlecome to python class {name}")

firstNumber = int(input('enter first number: '))
secondNumber = int(input('enter second number: '))

try:
    print(f'{firstNumber} divided by {secondNumber} is {firstNumber/secondNumber}')
except ZeroDivisionError as e:
    print("you cannot divide a number by zero(0)")
except:
    print("something really went wrong")
finally:
    print('this always runs on success of failure')
