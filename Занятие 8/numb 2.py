m=int(input('Введите количество элементов массива '))
def ms(m):
    massiv=[int(input()) for i in range (m)]
    print('Ваш массив = ', massiv)
    c=0
    for i in range (m):
        c=massiv[0]
        massiv[0]=massiv[i]
        massiv[i]=c
    print('Ваш новый массив = ', massiv)
ms(m)