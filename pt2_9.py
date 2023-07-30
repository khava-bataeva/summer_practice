a = int(input('Введите число, в котором все цифры различны: '))
a = str(a)
arr = []
for i in a:
    arr.append(i)
print(arr.index(max(arr)) + 1)
arr.reverse()
print(arr.index(max(arr)) + 1)
