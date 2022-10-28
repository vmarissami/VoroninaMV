n = int(input("Введите количество чисел из ряда"))
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
print((fibonacci(n + 2) - 1))
fibonacci(n)
# 1 1 2 3 5 8 13 21