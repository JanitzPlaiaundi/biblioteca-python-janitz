from model.book import Book
from controllers.log_controller import Log_controller
class BookController:
    def __init__(self):
        self.books = []
        self.logger = Log_controller()

    def load_books(self):
        self.books = []
        try:
            with open("data/books.txt", "r",encoding="utf-8") as f:
                for line in f:
                    if(line == ""):
                        break
                    book_info = line.split("|")
                    book = Book(int(book_info[0]), book_info[1], book_info[2], int(book_info[3]), book_info[4], book_info[5].strip())
                    self.books.append(book)
                return "Libros cargados correctamente"
        except FileNotFoundError as e:
            return e

    def write_books(self):
        with open("data/books.txt", "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(f"{str(book.code)}|{book.title}|{book.author}|{str(book.year)}|{book.category}|{book.state}\n")
        return "Se han actualizado los libros con exito"
    
    def list_books(self):
        return self.books

    def available_books(self):
        available_books_list = []
        for book in self.books:
            if book.state == "Libre":
                available_books_list.append(book)
        return available_books_list


    def search_by_name(self, word):
        books_searched = []
        for book in self.books:
            if word.lower() in book.title.lower():
                books_searched.append(book)
        return books_searched


    def search_by_id(self, id):
        try:
            for book in self.books:
                if id == book.code:
                    return book
        except:
            raise

    def lend_book(self, book_id):
        try:
            book = self.search_by_id(book_id)
            book.state = "Ocupado"
        except Exception as e:
            return e

    def return_book(self, book_id):
        try:
            book = self.search_by_id(book_id)
            book.state = "Libre"
        except:
            raise

    def create_book(self, title, author, year, category):
        try:
            code = self.books[-1].code + 1
            book = Book(code, title, author, year, category, "Libre")
            self.books.append(book)
            self.logger.write_log(f'Se ha añadido un nuevo libro')
        except:
            raise