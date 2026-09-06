#!/usr/bin/python3
import math 

print("welcome to pycalc")
print("exit pycalc with the exit operation")
print("reset pycalc with the reset operation")

try:    
    num_1 = float(input("enter first number: "))
except ValueError:
    print("please put a integer or a decima")

result = 0    

while True:

    try:
        operation = str(input("type operation symbol: "))
    except ValueError:
        print("please enter a valid operation")

    if operation not in ["+", "-", "*", "/", "%", "!", "perc", "exit", "reset", "sqrt" ]: 
        print("that operation isnt valid or it isnt included in pycalc")  
        num_1 = float(input("enter first number: "))
        continue

    if operation == "exit":
        break

    if operation == "reset":
        num_1 = float(input("enter first number: "))
        continue

    if operation == "sqrt":
        if num_1 < 0:
            print("you cant take negative sqrts")
            continue

        result = math.sqrt(num_1)
        print(result)
        num_1 = result
        continue

    if operation == "!":
        if num_1 < 0 or not num_1.is_integer():
            print("you cant take decimal/negative factorials")
            continue

        result = math.factorial(int(num_1))
        print(result)
        num_1 = result
        continue
    try:    
        num_2 = float(input("enter second number: "))
    except ValueError:
        print("thats not a valid number or decimal")

    if operation == "+":
        result =  num_1 + num_2

    if operation == "-":
        result =  num_1 - num_2

    if operation == "*":
        result =  num_1 * num_2

    if operation == "/":
        result =  num_1 / num_2

    if operation == "%":
        if num_2 == 0:
            print("you cant do a modulo of zero")
            continue
        result =  num_1 % num_2
    
    if operation == "perc":
        result = (num_1 / 100) * num_2

    print(result)

    num_1 = result
    
