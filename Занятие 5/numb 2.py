n=int(input('Введите число'))
def funct(n):
    i = 1
    while i<=n:
        i += 1
        if n%i==0:
            print(i)
            break
funct(n)