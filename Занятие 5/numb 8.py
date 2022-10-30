a = int(input())
def funct(a):
    k = 0
    max=1
    while a != 0:
        b=int(input())
        if a==b:
            k+=1
        else:
            if k>max:
                max=k
                k=0
        a=b
    print(max)
funct(a)