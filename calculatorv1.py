#!/usr/bin/python3
print("welcome to pycalc!!!")
print("use the command exit in operation prompt to exit pycalc")
print("use the command reset in operation prompt to restart pycalc")
num_1 = int(input("enter first number: "))

while True:


    operation = str(input("type operation symbol: "))
    result = 0

    if operation == "exit":
        break

    if operation == "reset":
        num_1 = int(input("enter first number: "))
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
