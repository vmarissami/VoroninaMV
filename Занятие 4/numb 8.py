n=int(input('Введите натуральное число'))
def funct(n):
    if n<0 and n>=9:
        print ('Это не натуральное число или оно больше 9')
    else:
        for i in range(1, n+1):
            for m in range (1, i+1):
                print(m, sep="", end="")
            print(" ")
funct(n)