a=int(input())
b=int(input())
def funct(a, b):
    if a > b:
        for i in reversed (range(b, a + 1)):
            if i%2!=0:
                print(i, end=";")
funct(a, b)