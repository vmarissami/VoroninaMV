a=int(input())
b=int(input())
l=int(input())
N=int(input())
def shnr(a, b, l, N):
    return ((a*N*2-a)+((b*(N-1))*2)+2*1)
print(shnr(a, b, l, N))