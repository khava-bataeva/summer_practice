n = int(input('Введите число: '))
for i in range(n):
    if i ** 2 > n:
        print(i)
        break
