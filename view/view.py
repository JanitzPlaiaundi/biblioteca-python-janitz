from exceptions.OutOfMenuRangeError import OutOfMenuRangeError
class View:
    def __init__(self, bookController, partnerController):
        self.bookController = bookController
        self.partnerController = partnerController

    

    def menu_options(self):
        print("Selecciona escribiendo con números las siguientes acciones: ")
        print("1. Listar todos los libros")
        print("2. Listar libros disponibles")
        print("3. Buscar libro por titulo")
        print("4. Asignar libro a socio")
        print("5. Devolver libro de un socio")
        print("6. Mostrar socios con libro")
        print("7. Añadir libro")
        print("8. Añadir socio")
        print("9. Salir del programa")


        while True:
            firstOption = 1
            lastOption = 9
            try:
                option = int(input("Opción: "))
                if option < firstOption or option > lastOption:
                    raise OutOfMenuRangeError("Opcion invalida, el número debe estar entre " + str(firstOption) + " y " + str(lastOption) + ".", option)
                else:
                    return option
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
            except OutOfMenuRangeError as e:
                print("Error: ",e)
                print("Valor incorrecto ingresado: ", e.value)

    def menu(self):
        num = 0
        while num != 9:
            num = self.menu_options()
            match num:
                case 1:
                    self.show_books()
                case 2:
                    self.available_books()
                case 3:
                    self.search_book_by_name()
                case 4:
                    self.assign_book_to_partner()
                case 5:
                    self.return_book()
                case 6:
                    self.show_partners_with_books()
                case 7:
                    pass
                case 8:
                    pass
                case 9:
                    pass
                case _:
                    print("Opción no válida.")

    def print_book(self, book):
        print(f'{book.code} | {book.title}')

    def print_partner(self, partner):
        print(f'{partner.code}|{partner.name}|{partner.email}|{partner.phone}|{','.join(partner.books)}')

    
    def print_list(self, list, format= "default" ):
        if format == "default":
            for string in list:
                print(string)

        if format == "book":
            for book in list:
                self.print_book(book)

        if format == "partner":
            for partner in list:
                self.print_partner(partner)
        

    def show_books(self):
        books = self.bookController.list_books()
        self.print_list(books, "book")
    
    def available_books(self):
        books = self.bookController.available_books()
        for book in books:
            print(book)

    def search_book_by_name(self):
        word_to_search = input("Escribe el nombre: ")
        books = self.bookController.search_by_name(word_to_search)
        if len(books) > 0:
            self.print_list(books, "book")
        else:
            print("No se ha encontrado ningun libro con ese nombre")

    def assign_book_to_partner(self):
        book_id = input("Escribe el código del libro: ")
        partner_id = input("Escribe el código del socio: ")
        partner_res = self.partnerController.assign_book(book_id, partner_id)
        book_res = self.bookController.lend_book(book_id)
        print(partner_res)
        print(book_res)


    def return_book(self):
        book_id = input("Escribe el código del libro: ")
        partner_id = input("Escribe el código del socio: ")
        partner_res = self.partnerController.return_book(book_id, partner_id)
        book_res = self.bookController.return_book(book_id)
        print(partner_res)
        print(book_res)

    def show_partners_with_books(self):
        partners = self.partnerController.partners_with_book()

        if len(partners) > 0:
            self.print_list(partners, "partner")
        else:
            print("No hay socios con libro")