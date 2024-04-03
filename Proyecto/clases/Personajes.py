from clases.ataques import *

class Personaje():
    def __init__(self, nombre, descripcion, vida, fuerza, velocidad, iq, ataques):
        self.nombre = nombre
        self.descripcion = descripcion
        self.vida = int(vida)
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.iq = iq
        self.ataques = ataques #Lista de instancias de ataques

    def mostrar_info(self):
        print (f"""{self.nombre}: 
        Vida: {self.vida}
        Fuerza: {self.fuerza}
        Velocidad: {self.velocidad}
        IQ: {self.iq}""")


class gallo_fortachon(Personaje):
    def __init__(self):
        super().__init__("Gallo Fortachon",
                         "Es capaz de dar golpes duros pero su velocidad se ve afectada por su robustez. No es muy inteligente y tiene mucha vida",
                         50, 6, 5, 4, [fuerza_bruta(), artilleria_pesada(), pollo_al_spiedo()])

class gallo_volador(Personaje):
    def __init__(self):
        super().__init__("Gallo Volador", "Vuelo gracil que le permite atacar mas rapido pero con fuerza limitada", 35,
                         4, 8, 6, [alas_fuertes(), pollo_a_tierra(), paracaidas()])

class gallo_sabio(Personaje):
    def __init__(self):
        super().__init__("Gallo Sabio", "Emplea toda su sabiduria esquivando ataques, sin embargo tiene una vida corta",
                         30, 5, 6, 8, [pico_sabio(), graznido_feroz(), golpe_equilibrado()])

class gallina(Personaje):
    def __init__(self):
        super().__init__("Gallina",
                         "Persevera y triunfaras, tiene todo lo que se debe tener para una batalla equilibrada", 40, 5,
                         7, 5, [picotazo(), ponedora(), pechuga_asada()])

class gallo_jefe(Personaje):
    def __init__(self):
        super().__init__("Gallo en Jefe", "El es el jefe", 45, 9, 9,
                         [fuerza_bruta(), artilleria_pesada(), pollo_al_spiedo(), alas_fuertes(), pollo_a_tierra(),
                          paracaidas(), pico_sabio(), graznido_feroz(), golpe_equilibrado(), picotazo(), ponedora(),
                          pechuga_asada()])

