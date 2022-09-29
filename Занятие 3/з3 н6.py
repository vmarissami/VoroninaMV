s1=int(input())
k1=int(input())
s2=int(input())
k2=int(input())
def xxx(s1, k1):
    return (s1+k1)%2
def yyy(s2, k2):
    return (s2+k2)%2
if (xxx(s1, k1)==0 and yyy(s2, k2)==0) or (xxx(s1, k1)==1 and yyy(s2, k2)==1):
    print ('Да')
else:
    print ('Нет')