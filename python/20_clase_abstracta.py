from abc import ABC, abstractmethod

class NaveEspacial(ABC):
    modelo:str
    def __init__(self, modelo:str):
        self.modelo=modelo

    @abstractmethod
    def despegar(self):
        pass
    
class NaveCapsula(NaveEspacial):
    modelo:str
    def __init__(self, modelo:str):
        super.modelo=modelo
        
    def despegar(self):
        print(self.modelo,"despega con motores de capsule corp")

class Navesaiyajin(NaveEspacial):
    def __init__(self, modelo:str):
        super().__init__(modelo)
        
    def despegar(self):
        print(self.modelo,"despega imediatamente")
        
nave_bulma=NaveCapsula("nave de bulma")
nave_vegeta=Navesaiyajin("nave de vegeta")
nave_bulma.despegar()
nave_vegeta.despegar()