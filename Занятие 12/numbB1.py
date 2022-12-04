numb=int(input('Введите число '))
def funct(numb, max):
    max=numb
    while numb!=0:
        numb=int(input('Введите число '))
        if numb>max:
            max=numb
    print(max)
funct(numb, max)