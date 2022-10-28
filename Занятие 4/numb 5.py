n=int(input('Введите натуральное число'))
def funct(n):
    s=0
    if n<0:
        print ('Это не натуральное число!')
    else:
        for i in range(n+1):
            c=i**3
            s+=c
        print(s)
funct(n)


