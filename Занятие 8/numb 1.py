n=int(input('Сколько чисел вы хотите проверить? '))
def funct(n):
    for a in str (n):
        if a=='0' or n%int(a):
            return False
    return True
for i in range(1, n+1):
    if funct(i):
        print(i)