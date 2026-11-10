from model.book import Book


class BookController:
    def __init__(self):
        pass

    def charge_books(self):
        books = []
        try:
            with open("data/books.txt", "r",encoding="utf-8") as f:
                for line in f:
                    if(line == ""):
                        break
                    book_info = line.split("|")
                    book = Book(book_info[0], book_info[1], book_info[2], book_info[3], book_info[4], book_info[5].strip())
                    books.append(book)
                return books
        except FileNotFoundError as e:
            print(e.strerror)

    def available_books(self):
        available_books_list = []
        books = self.charge_books()
        for book in books:
            if book.state == "Libre":
                available_books_list.append(book)
        return available_books_list


    #Devuelve el primer libro con la palabra    
    def search_by_name(self, word):
        books = self.charge_books()
        books_searched = []
        for book in books:
            if word.lower() in book.title.lower():
                books_searched.append(book)

        return books_searched