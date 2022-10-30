n=int(input('Введите число'))
def funct(n):
    s = 1
    while n>(2**s):
        s += 1
    print(s-1, 2**(s-1))
funct(n)