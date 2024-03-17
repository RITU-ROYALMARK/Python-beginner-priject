#algoritms to find the biggest number

class find:
    def __init__(self,num,num1,num2):
        self.num = num
        self.num1 = num1
        self.num2 = num2
    def find_biggest(self):
        if self.num > self.num1 and self.num > self.num2:
            return "first IS BIG"
        elif self.num1 > self.num and self.num > self.num2:
            return "middle IS BIG"
        else:
            return "last IS BIG"

F = find(20,40,57)
print(F.find_biggest())