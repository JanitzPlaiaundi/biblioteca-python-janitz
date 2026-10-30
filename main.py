from model.book import Book
from exceptions.OutOfMenuRangeError import OutOfMenuRangeError

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

def menu():
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
                print("numero valido")
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
        except OutOfMenuRangeError as e:
            print("Error: ",e)
            print("Valor incorrecto ingresado: ", e.value)
menu()