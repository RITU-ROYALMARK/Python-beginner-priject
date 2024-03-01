"""" write a programme to print * sign before a ( bracket like if the question is
3(2+4) and the output should be like 3 * (2+4) or
EXAMPLE:-
    input:- 3(2a+4b)

    output:- 3*(2a+4b)
"""

def add_input(num):
    result = ''
    for position in range(len(num)):
        if num[position] == '(':
            s1 = num.index(")")
            result = result+'*'+num[position:s1+1]
            break
        else:
            result += num[position]
    return result




try:
    num = input("enter the value: ")
    print(add_input(num))
except ValueError:
    print("TYPE A NUMBER")

