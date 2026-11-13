# 📚 Sistema de Gestión de Biblioteca

Aplicación de consola desarrollada en Python bajo una arquitectura modular inspirada en el patrón **MVC (Modelo-Vista-Controlador)** para administrar el catálogo de libros, el registro de socios y el control de préstamos mediante persistencia en ficheros de texto plano (`.txt`).

## 🚀 Funcionalidades de la Aplicación

La aplicación permite realizar las siguientes operaciones desde un menú interactivo en consola:

* **Gestión de Libros:**
  * Listar todos los libros registrados en el catálogo.
  * Consultar únicamente los libros disponibles para préstamo.
  * Buscar libros por coincidencia en el título.
  * Dar de alta nuevos libros (título, autor, año de lanzamiento y categoría).
* **Gestión de Socios:**
  * Registrar nuevos socios con asignación automática de código identificativo.
  * Consultar qué socios tienen libros actualmente en préstamo.
* **Control de Préstamos y Persistencia:**
  * Asignar un libro disponible a un socio y registrar su devolución.
  * Cargar los datos automáticamente al iniciar la aplicación desde `data/books.txt` y `data/partners.txt`, y guardar los cambios al salir del programa.
  * Validar las opciones de los menús mediante excepciones personalizadas (`OutOfMenuRangeError`).

---

## 🛠️ Puntos de Mejora a Futuro (Roadmap)

A partir de la revisión del código actual, estas son las principales mejoras recomendadas para escalar y blindar la aplicación:

1. **Integridad Transaccional en Préstamos y Devoluciones:**
   * *Problema actual:* En `assign_book_to_partner()` y `return_book()`, la actualización del socio y del libro se ejecutan de forma independiente; si un código no existe, uno de los dos registros puede quedar modificado a medias.
   * *Mejora:* Verificar previamente que tanto el libro (y su estado disponible) como el socio existen antes de confirmar la operación.
2. **Validación Estricta de Datos de Entrada:**
   * *Mejora:* Validar el formato de correo electrónico, teléfono numérico y año de lanzamiento al crear registros; impedir el uso del carácter delimitador `|` en los textos para no corromper los `.txt`; y sustituir los bloques `except:` genéricos por excepciones específicas (`ValueError`, `FileNotFoundError`, `OSError`).
3. **Evolución del almacenamiento:**
   * *Mejora:* Migrar el almacenamiento plano a `JSON` o `SQLite` (nativos en Python) para consultas más robustas.

---

## 🏗️ Estructura del Proyecto

```text
biblioteca/
├── controllers/
│   ├── book_controller.py      # Lógica de negocio y persistencia de libros
│   └── partner_controller.py   # Lógica de negocio y persistencia de socios
│   └── log_controller.py       # Control de acciones mediante logs
├── data/
│   ├── books.txt               # Almacenamiento plano de libros (delimitador |)
│   └── partners.txt            # Almacenamiento plano de socios y préstamos
│   └── logs.txt                # Almacenamiento plano de logs
├── exceptions/
│   └── OutOfMenuRangeError.py  # Excepción personalizada para validación de rangos
├── model/
│   ├── book.py                 # Entidad Book
│   └── partner.py              # Entidad Partner
├── view/
│   └── view.py                 # Interfaz de consola y gestión dinámica de menús
└── main.py                     # Punto de entrada de la aplicación
└── readme.md                   # Información sobre el proyecto y guia de uso
```

## ⚙️ Requisitos y Ejecución

* **Requisitos:** Python 3.10 o superior (necesario para el uso de `match / case`). No requiere dependencias externas.
* **Ejecución:** Desde la raíz del proyecto, asegurándose de que existe la carpeta `data/` con los ficheros `books.txt` y `partners.txt`:

```bash
python main.py
```