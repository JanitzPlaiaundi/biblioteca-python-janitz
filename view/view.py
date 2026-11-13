from exceptions.OutOfMenuRangeError import OutOfMenuRangeError
class View:
    def __init__(self, bookController, partnerController):
        self.bookController = bookController
        self.partnerController = partnerController

    def execute(self):
        try:   
            print(self.bookController.load_books())
            print(self.partnerController.load_partners())
            self.menu()
        except Exception as e:
            print(e)


    #MENUS

    main_menu_options = [
        "Selecciona escribiendo con números las siguientes acciones: ",
        "Listar todos los libros",
        "Listar libros disponibles",
        "Buscar libro por titulo",
        "Asignar libro a socio",
        "Devolver libro de un socio",
        "Mostrar socios con libro",
        "Añadir socios o libros",
        "Salir del programa"
    ]    

    create_menu_option = [
        "Selecciona escribiendo con números las siguientes acciones: ",
        "Crear socio",
        "Crear libro",
        "Volver atras"
    ]

    def menu(self):
        num = 0
        while num != 8:
            num = self.menu_options(self.main_menu_options)
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
                    create_option = self.menu_options(self.create_menu_option)
                    match create_option:
                        case 1:
                            self.create_partner_view()
                        case 2:
                            self.create_book_view()
                        case _:
                            pass
                case 8: 
                    print(self.partnerController.write_partners())
                    print(self.bookController.write_books())
                case _:
                    print("Opción no válida.")

    def menu_options(self, options):
            while True:
    
                for i, option in enumerate(options):
                    if i == 0:
                        print(option)
                    else:
                        print(f'{i}. {option}')
    
                firstOption = 1
                lastOption = len(options) - 1
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

    #Pintar con formatos
    def print_book(self, book):
        print(f'Libro {book.title}:')
        print(f'    Codigo: {book.code}')
        print(f'    Titulo: {book.title}')
        print(f'    Año de lanzamiento: {book.year}')
        print(f'    Categoria: {book.category}\n')

    def print_partner(self, partner):
        print(f'Socio {partner.name}:')
        print(f'    Codigo: {partner.code}')
        print(f'    Nombre: {partner.name}')
        print(f'    Email: {partner.email}')
        print(f'    Telefono: {partner.phone}\n')

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

    #Recoger o modificar datos
    def show_books(self):
        books = self.bookController.list_books()
        self.print_list(books, "book")
    
    def available_books(self):
        books = self.bookController.available_books()
        self.print_list(books, "book")

    def search_book_by_name(self):
        word_to_search = input("Escribe el nombre: ")
        books = self.bookController.search_by_name(word_to_search)
        if len(books) > 0:
            self.print_list(books, "book")
        else:
            print("No se ha encontrado ningun libro con ese nombre")

    def assign_book_to_partner(self):
        try:
            book_id = int(input("Escribe el código del libro: "))
            partner_id = int(input("Escribe el código del socio: "))
            self.partnerController.assign_book(book_id, partner_id)
            self.bookController.lend_book(book_id)
            print("Libro asignado correctamente")
        except Exception as e:
            print("Error al reservar el libro")

    def return_book(self):
        try:
            book_id = int(input("Escribe el código del libro: "))
            partner_id = int(input("Escribe el código del socio: "))
            self.partnerController.return_book(book_id, partner_id)
            self.bookController.return_book(book_id)
            print("Libro devuelto correctamente")
        except Exception as e:
            print("Error al devolver el libro")


    def show_partners_with_books(self):
        partners = self.partnerController.partners_with_book()
        if len(partners) > 0:
            self.print_list(partners, "partner")
        else:
            print("No hay socios con libro")


    def create_partner_view(self):
        try:
            name = input("Nombre: ")
            email = input("Email: ")
            phone = input("Numero: ")
            self.partnerController.create_partner(name, email, phone)
            print("Socio creado correctamente")
        except:
            print("Error al crear el socio")

    def create_book_view(self):
        try:
            title = input("Titulo: ")
            author = input("Autor: ")
            year = input("Año de lanzamiento: ")
            category = input("Categoria: ")
            self.bookController.create_book(title, author, year, category)
            print("Libro añadido correctamente")
        except:
            print("Error al añadir el libro")