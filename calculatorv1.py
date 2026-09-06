#!/usr/bin/python3
import math 
try:    
    print("welcome to pycalc!!!")

    print("use the command exit in operation prompt to exit pycalc")
    print("use the command reset in operation prompt to restart pycalc")

    num_1 = float(input("enter first number: "))

    sqrt_result = 0

    result = 0 

    while True:


        operation = str(input("type operation symbol: "))

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
            if num_1 < 0:
                print("you cant take negative factorials")
                continue
            result = math.factorial(num_1)
            print(result)
            num_1 = result
            continue
        num_2 = float(input("enter second number: "))


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
except ValueError:
    print("please type a valid operation/number")
except ZeroDivisionError:
    print("you cant divide by zero")
