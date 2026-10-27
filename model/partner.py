class Partner:
    def __init__(self, code, name, email, phone, books = []):
        self.code = code
        self.name = name
        self.email = email
        self.phone = phone
        self.books = books

    def __str__(self):
        return f'Información del socio "{self.name}":\n  Codigo: {self.code}\n  Nombre: {self.name}\n  Email: {self.email}\n  Teléfono: {self.phone}\n  Libros: {", ".join([book.title for book in self.books])}'