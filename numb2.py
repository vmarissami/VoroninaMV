import numpy as np
n=int(input())
a=[]
def f(a):
    for i in range(n):
        b=[]
        for j in range(n):
            print('введите [', i,',',j, ']элемент')
            b.append(int(input()))
        a.append(b)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    transpose=np.transpose(a)
    print()
    print(transpose)
f(a)