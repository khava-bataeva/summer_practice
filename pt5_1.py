import csv

header = ["Книга", "Автор", "Год выпуска"]
rows = [["Война и мир", "Лев Толстой", "1865"],
        ["Отверженные", "Виктор Гюго", "1862"],
        ["Мёртвые души", "Николай Гоголь", "1842"],
        ["Мастер и Маргарита", "Михаил Булгаков", "1937"]]

filename = "prog_books.csv"

with open(filename, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
