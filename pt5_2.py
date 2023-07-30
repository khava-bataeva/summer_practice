import csv

def bookslist(num):
    books = []
    for _ in range(num):
        name = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        year = input('Введите год выпуска книги: ')
        books.append({'Название': name, 'Автор': author, 'Год выпуска': year})
    return books

def find_books(books, author):
    matching = []
    for book in books:
        if book['Автор'] == author:
            matching.append(book)
    return matching

num = int(input('Сколько записей вы хотите добавить в список? '))

books = bookslist(num)

author = input('Введите автора книги, которую вы хотите найти: ')

matching = find_books(books, author)

if matching:
    print(f'Книги автора {author}:')
    for book in matching:
        print(f'Название: {book["Название"]}, Год выпуска: {book["Год выпуска"]}')
else:
    print(f'Нет книг автора {author} в списке.')

with open('books.csv', 'w', newline='') as csvfile:
    fieldnames = ['Название', 'Автор', 'Год выпуска']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(books)

