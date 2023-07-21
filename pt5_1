import csv

def create():
    books = [
        {'Название': 'Ревизор', 'Автор': 'Николай Гоголь', 'Год выпуска': 1836},
        {'Название': 'Преступление и наказание', 'Автор': 'Фёдор Достоевский', 'Год выпуска': 1866},
        {'Название': 'Пиковая дама', 'Автор': 'Александр Пушкин', 'Год выпуска': 1834},
        {'Название': 'Ася', 'Автор': 'Иван Тургенев', 'Год выпуска': 1858}
    ]

    with open('books.csv', 'w', newline='') as csvfile:
        fieldnames = ['Название', 'Автор', 'Год выпуска']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for book in books:
            writer.writerow(book)

create()
