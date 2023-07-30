n = int(input('Введите число: '))
s = 0
while n < 0:
    s += n
    n = int(input('Введите число: '))
print(s)
