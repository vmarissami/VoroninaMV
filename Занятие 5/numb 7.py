a = int(input())
def funct(a):
    k = 0
    while a != 0:
        b=int(input())
        if a!=0 and a<b:
            k+=1
        a=b
    print(k)
funct(a)
