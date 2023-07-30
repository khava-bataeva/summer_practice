import csv


def csv_add_row(filename1, row1):
    with open(filename1, "a", encoding="utf-8") as f1:
        writer = csv.writer(f1)
        writer.writerow(row1)


filename = "prog_books.csv"

n_rows = int(input("Сколько записей вы ходите добавить?: "))
for i in range(n_rows):
    print(f"Добавление записи {i+1}")
    book = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = input("Введите год выпуска: ")
    row = [book, author, year]
    csv_add_row(filename, row)
    print("Запись добавлена.\n")

name = input("Введите автора для поиска его книг: ")
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    found = False
    for row in reader:
        if name in row["Автор"]:
            found = True
            print(row["Книга"], row["Автор"], sep=", ")
    if not found:
        print("Книги не найдены.")
