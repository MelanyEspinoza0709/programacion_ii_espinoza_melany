class RadarDragon:
    region1: int
    region2: int
    def __init__(self, region1,region2):
        self.region1 = region1
        self.region2 = region2

    def buscar_esferas1(self, cantidad):
        esferas1= self.region1 * cantidad
        print("esferas encontradas en region1:",self.region1)
        print("esferas:", esferas1)

    def buscar_esferas2(self, cantidad):
        esferas2 = self.region2 * cantidad
        print("esferas encontradas en region2:",self.region2)
        print("esferas:",esferas2)
        
radar_bulma = RadarDragon(3, 2)
radar_bulma.buscar_esferas1(1)
radar_bulma.buscar_esferas2(1)

