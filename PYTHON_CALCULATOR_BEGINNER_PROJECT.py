# BUILD A SIMPLE CALCULATOR IN PYTHON BEGINNER PROJECT

def calculator(num,op,num1):
    exec = eval(f"{num}{op}{num1}")
    return exec

try:
    num = input("enter: ")
    op = input("enter op: ")
    num1 = input("enter num1: ")
    calc = calculator(num,op,num1)
    print(calc)
except ValueError:
    print("TYPE INT NOT ANY OTHER DATATYPES")


