class Book:
    def __init__(self, code, title, author, year, category, state = "Libre"):
        self.code = code
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.state = state

    def __str__(self):
        return f'Información del libro "{self.title}":\n  Codigo: {self.code}\n  Titulo: {self.title}\n  Autor: {self.author}\n  Año de creación: {self.year}\n  Categoria: {self.category}\n  Socio: {self.state}'