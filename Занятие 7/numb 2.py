a=int(input('Сколько чисел вы хотите ввести? '))
def ms(a):
    massiv=[int(input()) for i in range (a)]
    for item in massiv:
        if item==0:
            massiv.remove(0)
            massiv.append(sum(massiv)/a)
            print(massiv)
ms(a)
