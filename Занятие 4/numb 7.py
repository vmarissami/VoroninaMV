n=int(input('Введите натуральное число'))
def funct(n):
    p=1
    s=0
    if n<0:
        print ('Это не натуральное число!')
    else:
        for i in range(1, n+1):
            p*=i
            s+=p
        print(s)
funct(n)