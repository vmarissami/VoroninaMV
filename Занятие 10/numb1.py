import os
def getpath(path):
  return os.path.realpath(os.path.join(__file__, '..' ,path))
def vvod(filename=getpath('voronina_vvod.txt')):
  matr=[]
  with open(filename, 'r') as file:
    for line in file:
      matr.append(list(map(int, line.strip().split(' '))))
  return matr
def vivod(answer, filename=getpath('voronina_vivod.txt')):
  with open(filename, 'w') as file:
    file.write(answer)
import numpy as np
def f(k):
  a=vvod()
  print(a)
  answer_string = ''
  for n in range(0, len(a)):
    print(a[k][n], ':', a[n][n], '=', a[k][n]/a[n][n])
    answer_string += str(a[k][n]/a[n][n]) + '\n'
  vivod(answer_string)
f(int(input('Введите k: ')) - 1)