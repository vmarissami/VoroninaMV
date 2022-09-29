n=int(input())
m=int(input())
k=int(input())
def kus(n, m):
    if ((k%n==0)or(k%m==0)) and k<(n*m):
        return 'Да'
    else:
        return 'Нет'
print(kus(n, m))