import os
def getpath(path):
  return os.path.realpath(os.path.join(file, '..' ,path))
def vvod(filename=getpath('voronina_vvod.txt')):
  matr=[]
  with open(filename, 'r') as file:
    for line in file:
      matr.append(list(map(int, line.strip().split(' '))))
  return matr
def vivod(answer, filename=getpath('voronina_vivod.txt')):
  with open(filename, 'w') as file:
    file.write(str(answer))

import numpy as np
a=vvod()
def f(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end=' ')
        print()
    transpose=np.transpose(a)
    print()
    print(transpose)
    vivod(transpose)
f(a)