from exceptions.OutOfMenuRangeError import OutOfMenuRangeError
class View:
    def __init__(self, bookController, partnerController):
        self.bookController = bookController
        self.partnerController = partnerController

    def menu_options(self):
        print("Selecciona escribiendo con numeros las siguientes acciones: ")
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
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
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

    def print_list(self, list, format= "default" ):
        if format == "default":
            for string in list:
                print(string)

        if format == "book":
            for book in list:
                self.print_book(book)

        

    def show_books(self):
        books = self.bookController.charge_books()
        self.print_list(books, "book")
    
    def available_books(self):
        books = self.bookController.available_books()
        for book in books:
            print(book)