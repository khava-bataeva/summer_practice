def count(str):
    count_letter = {letter: str.count(letter) for letter in str if letter != ' '}
    return count_letter


str = input('Введите строку: ')
res = count(str)
print('Словарь, содержащий буквы и их количество:')
print(res)
