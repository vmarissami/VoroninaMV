a=int(input('Введите а '))
b=int(input('Введите b '))
def funct(a, b):
    if a%b==0:
        return 0
    return a%b
print(a%b)
funct(a, b)