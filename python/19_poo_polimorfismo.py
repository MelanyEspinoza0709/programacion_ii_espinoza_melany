class Guerrero:
    nombre:str
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        self.nombre=nombre
        self.poder_inicial=poder_inicial
        self.horas=horas
    def atacar(self):
        print(f"{self.nombre} realiza un ataque")
    def calcular_poder(self):
        return self.poder_inicial

class goku(Guerrero):
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        super().__init__(nombre, poder_inicial, horas)
    def atacar(self):
        print(self.nombre,"uliliza kamehameha")
        
    def calcular_poder(self):
        return self.poder_inicial+self.horas*100
        
class vegeta(Guerrero):
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        super().__init__(nombre, poder_inicial, horas)
    def atacar(self):
        print(self.nombre,"utiliza final flash")
    def calcular_poder(self):
        return self.poder_inicial+self.horas*150 

goku=goku("gran goku", 150,50)
vegeta=vegeta("vegeta",200,80)
goku.atacar()
vegeta.atacar()
print (goku.calcular_poder())
print (vegeta.calcular_poder())