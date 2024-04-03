
class ataque():
    def __init__(self, nombre_ataque, fuerza_ataque, velocidad_ataque):
        self.nombre = nombre_ataque
        self.fuerza = int(fuerza_ataque)
        self.velocidad = int(velocidad_ataque)

    def presentar_ataque(self):
        return f"{self.nombre}: fuerza {self.fuerza}, velocidad {self.velocidad}"

    def obtener_fuerza (self):
        return self.fuerza

    def obtener_velocidad (self):
        return self.velocidad


        """LOS ATAQUES DE GALLO FORTACHON"""
class fuerza_bruta(ataque):
    def __init__(self):
        super().__init__("Fuerza Bruta", 8, 2)
class artilleria_pesada(ataque):
    def __init__(self):
        super().__init__("Artilleria Pesada", 6, 4)
class pollo_al_spiedo (ataque):
    def __init__(self):
        super().__init__("Fuerza Bruta", 4, 6)

        """LOS ATAQUES DE GALLO VOLAADOR"""
class alas_fuertes (ataque):
    def __init__(self):
        super().__init__("Alas Fuertes", 7, 3)
class pollo_a_tierra(ataque):
    def __init__(self):
        super().__init__("Pollo a tierra", 6,4 )
class paracaidas (ataque):
    def __init__(self):
        super().__init__("Paracaidas", 4,6)

        """LOS ATAQUES DE GALLO SABIO"""
class pico_sabio(ataque):
    def __init__(self):
        super().__init__("Pico Sabio", 3,7)
class graznido_feroz (ataque):
    def __init__(self):
        super().__init__("Graznido Feroz", 7,3)
class golpe_equilibrado(ataque):
    def __init__(self):
        super().__init__("Golpe Equilibrado", 5,5)

        """LOS ATAQUES DE GALLINA"""
class picotazo(ataque):
        def __init__(self):
            super().__init__("Picotazo", 4,6)
class ponedora (ataque):
        def __init__(self):
            super().__init__("Ponedora", 6,4)
class pechuga_asada(ataque):
        def __init__(self):
            super().__init__("Pechuga Asada", 8,2)




