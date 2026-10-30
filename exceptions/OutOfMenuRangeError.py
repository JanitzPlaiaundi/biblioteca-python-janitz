from email import message


class OutOfMenuRangeError(Exception):
    def __init__(self, message="Opción inválida. Por favor, selecciona un número entre 1 y 9.", value=None):
        super().__init__(message)
        self.value = value
        