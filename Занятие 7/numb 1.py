a=int(input('Сколько чисел вы хотите ввести? '))
def sp(a):
    spisok=[int(input()) for i in range (a)]
    print('Ваш список ', spisok)
    print('Сумма чисел в списке = ', sum(spisok))
sp(a)