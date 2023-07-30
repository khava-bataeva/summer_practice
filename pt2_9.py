n = int(input("Введите число: "))
def find_max(n):
    n_str = str(n)
    max_n = max(n_str)
    position1 = n_str[::-1].index(max_n) + 1
    position2 = n_str.index(max_n) + 1
    return position1, position2
result1, result2 = find_max(n)
print("Порядковый номер максимальной цифры (считая от конца числа):", result1)
print("Порядковый номер максимальной цифры (считая от начала числа):", result2)
