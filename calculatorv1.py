#!/usr/bin/python3
import math 
try:    
    print("welcome to pycalc!!!")

    print("use the command exit in operation prompt to exit pycalc")
    print("use the command reset in operation prompt to restart pycalc")

    num_1 = int(input("enter first number: "))

    sqrt_result = 0

    result = 0 

    while True:


        operation = str(input("type operation symbol: "))

        if operation == "exit":
            break

        if operation == "reset":
            num_1 = int(input("enter first number: "))
            continue

        if operation == "sqrt":
            sqrt_result = math.sqrt(num_1)
            result = sqrt_result
            print(result)
            num_1 = result
            continue

        if operation == "!":
            result = math.factorial(num_1)
            print(result)
            num_1 = result
            continue
        num_2 = int(input("enter second number: "))


        if operation == "+":
            result =  num_1 + num_2

        if operation == "-":
            result =  num_1 - num_2

        if operation == "*":
            result =  num_1 * num_2

        if operation == "/":
            result =  num_1 / num_2

        if operation == "%":
            result =  num_1 % num_2

        print(result)

        num_1 = result
except ValueError:
    print("please type a valid operation/number")
except ZeroDivisionError:
    print("you cant divide by zero")
