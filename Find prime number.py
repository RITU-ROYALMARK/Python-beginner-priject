# Check whether a number is prime or not

n = 0
i = 2
flage = 1

n = int(input("enter the n value: "))

while i <= (n / 2):

    if n % i == 0:
        flage = 0
        break
    i += 1

if flage == 0:
    print(f"{n}: is not a prime")
else:
    print(f"{n} is an prime")
