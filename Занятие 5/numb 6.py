a=int(input())
def funct(a):
    k=1
    sum=0
    while a>0:
        sum += a
        k+=1
        a = int(input())
    print(sum/k)
funct(a)