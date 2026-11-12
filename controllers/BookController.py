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


    def search_by_id(self, id):

        self.charge_books()
        for book in self.books:
            if id == book.code:
                return book
        return None

    def lend_book(self, book):
        book.state = "lent"
        return self.write_books()

    def write_books(self):
            with open("data/books.txt", "w", encoding="utf-8") as f:
                for book in self.books:
                    f.write(f"{book.code}|{book.title}|{book.author}|{book.year}|{book.category}|{book.state}\n")
            return "Se han actualizado los libros con exito"