h=0
def vremya(n):
    if 0<n<=59:
        return n
    if n>59:
        return n%60
def hrs(n):
    if 0<n<=59:
        return 0
    if n>59:
        return n%(60*24)//60
print(hrs(1500), vremya(1500))
