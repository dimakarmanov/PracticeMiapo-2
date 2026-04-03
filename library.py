import os

FILE_NAME = "books.txt"

def load_books():
    books = []
    if os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        books.append({"title": parts[0], "author": parts[1], "year": parts[2]})
    return books

def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for book in books:
            f.write(f"{book['title']}|{book['author']}|{book['year']}\n")

def show_books(books):
    if not books:
        print("\nНет книг\n")
        return
    print("\n" + "-" * 50)
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} - {book['author']} ({book['year']})")
    print("-" * 50 + f"\nВсего: {len(books)}\n")

def add_book(books):
    print("\n--- Добавление книги ---")
    title = input("Название: ").strip()
    if not title:
        print("Ошибка: нужно название\n")
        return
    author = input("Автор: ").strip()
    if not title:
        print("Ошибка: нужен автор\n")
        return
    year = input("Год: ").strip()
    if not title:
        print("Ошибка: нужен год\n")
        return

    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print(f"Книга '{title}' добавлена!\n")
