vowels = 'уеёыаоэяию'
consonants = 'йцкнгшщзхъфвпрлджчсмтьб'
s = input("Введите строку: ")
letter_dict = {letter: True if letter.lower() in vowels
               else False for letter in s if letter.isalpha()}
print(letter_dict)
