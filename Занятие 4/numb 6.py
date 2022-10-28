n=int(input('Введите натуральное число'))
def funct(n):
    p=1
    if n<0:
        print ('Это не натуральное число!')
    else:
        for i in range(1, n+1):
            p*=i
        print(p)
funct(n)