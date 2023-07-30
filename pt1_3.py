a = int(input('Введите число a '))
b = int(input('Введите число b '))
c = int(input('Введите число c '))
print('Максимальным числом является: ', end='')
if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif a <= c >= b:
    print(c)
if (b <= a >= c and b > c):
    print(a, b, c)
elif (b <= a >= c and c > b):
    print(a, c, b)
elif (a <= b >= c and a > c):
    print(b, a, c)
elif (a <= b >= c and c > a):
    print(b, c, a)
elif (a <= c >= b and a > b):
    print(c, a, b)
elif (a <= c >= b and b > a):
    print(c, b, a)
