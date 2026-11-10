from model.book import Book


class BookController:
    def __init__(self):
        self.books = []
        self.charge_books()

    def charge_books(self):
        self.books = []
        try:
            with open("data/books.txt", "r",encoding="utf-8") as f:
                for line in f:
                    if(line == ""):
                        break
                    book_info = line.split("|")
                    book = Book(book_info[0], book_info[1], book_info[2], book_info[3], book_info[4], book_info[5].strip())
                    self.books.append(book)
        except FileNotFoundError as e:
            print(e.strerror)

    def list_books(self):
        self.charge_books()
        return self.books

    def available_books(self):
        available_books_list = []
        self.charge_books()
        for book in self.books:
            if book.state == "Libre":
                available_books_list.append(book)
        return available_books_list


    def search_by_name(self, word):
        books_searched = []
        self.charge_books()
        for book in self.books:
            if word.lower() in book.title.lower():
                books_searched.append(book)

        return books_searched