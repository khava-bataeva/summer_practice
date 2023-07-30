import itertools


def chislo(numlist):
    s = ''.join(numlist)
    s = int(s)
    return s


a = input('Введите список чисел через пробел: ').split(' ')
suma = int(input('Введите число (сумму): '))
for i in range(1, len(a)):
    comb_set = itertools.combinations(a, i)
    for j in comb_set:
        n = list(j)
        s_arr = sum(list(map(int, j)))
        if s_arr == suma:
            print(chislo(n))
