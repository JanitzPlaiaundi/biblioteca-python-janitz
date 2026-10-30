from model.book import Book

def charge_books():
    books = []
    try:
        with open("data/books.txt", "r",encoding="utf-8") as f:
            for line in f:
                if(line == ""):
                    break
                book_info = line.split("|")
                book = Book(book_info[0], book_info[1], book_info[2], book_info[3], book_info[4], book_info[5])
                books.append(book)

    except FileNotFoundError as e:
        print(e.strerror)
    return books

for book in charge_books():
    print(book)