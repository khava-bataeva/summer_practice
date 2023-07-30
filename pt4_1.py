num = input("Введите число: ")
sorted_str = map(str, sorted(map(int, list(num)), reverse=True))
max_num = int(''.join(sorted_str))
print(max_num)
