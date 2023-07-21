import csv

with open("books.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) 
    start = int(input("Введите начальный год: "))
    end = int(input("Введите конечный год: "))
    count = 0
    for row in reader:
        year = int(row[2])
        if int(start) <= year <= int(end):
            print(row)
            count += 1
    if count == 0:
        print("Книги в данном временном отрезке не найдены")