# in this project we build a calculator using IF STATMENTS AND ELSE


try:
    while True:
        num1 = int(input("enter the number: "))
        operator = input("enter operator: ")
        num2 = int(input("enter the number2: "))
        if operator == "+":
            print(num1+num2)
        elif operator == "-":
            print(num1-num2)
        elif operator == "/":
            print(num1/num2)
        elif operator == "*":
            print(num1*num2)
        again = input("DO YOU WANNO GO AGAIN TYPE Y/N: ")
        if again.lower() != "y":
            print("THANK YOU FOR USING THE CALCULATORE")
            break

        else:
            continue
except (ValueError,TypeError):
    print("TYPE ERROR")