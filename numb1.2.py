import numpy as np
N=int(input('Введите количество элементов в строке (порядок) '))
k=int(input('Введите k '))-1
def f(N, k):
    a=np.random.randint(1, 10, size=(N, N))
    print(a)
    for n in range(0, len(a)):
        print(a[k, n], ':', a[k, k], '=', a[k, n]/a[n, n])
f(N, k)
#В этой программе элементы строки делятся только на диагональный элемент строки k
#В программе 1.1 элементы строки делятся на каждый элемент диагонали