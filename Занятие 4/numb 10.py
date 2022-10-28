n=int(input('Количество чисел из ряда Фибоначчи'))
k=int(input('Порядковый номер в ряду с которого надо начать'))
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
print((fibonacci(n + 2) - 1)-(fibonacci((k-1) + 2) - 1))
fibonacci(n)
# 1 1 2 3 5 8 13 21 34 55...
# Программа считает сумму чисел с k по n (надеюсь правильно поняла задачу)