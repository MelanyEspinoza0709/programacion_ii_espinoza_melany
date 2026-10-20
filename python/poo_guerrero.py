class Guerrero:
    nombre: str
    def __init__(self, nombre: str):
        self.nombre = nombre
    def presentarse(self):
        print("mi poderoso nombre es:", self.nombre)
