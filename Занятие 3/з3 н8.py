a=int(input())
b=int(input())
c=int(input())
def sovp(a, b, c):
    if a==b and b==c:
        return '3'
    elif a==b or b==c or c==a:
        return '2'
    else:
        return '0'
print(sovp(a, b, c))