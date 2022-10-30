n=int(input('Введите натуральное число'))
def funct(n):
    i = 1
    while i < n:
        print(i**2)
        i += 1
funct(n)