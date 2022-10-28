a=int(input())
b=int(input())
def funct (a, b):
        if a<b:
            for i in range(a, b+1):
                print(i, end=";")

        else:
            for i in reversed (range(b, a+1)):
                print(i, end=";")
funct(a, b)