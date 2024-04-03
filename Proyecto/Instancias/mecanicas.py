from random import randint
import sys

def elegir_ataque(ataques):
    while True:
        print("ELIGE UN ATAQUE")
        i = 1
        for ataque in ataques:
            print(f"{i}. {ataque.presentar_ataque()}")
            i += 1
        ataque_elegido = input("Seleccione un ataque: ")
        if ataque_elegido in ["1", "2", "3"]:  # Comparar con cadenas en lugar de enteros
            return int(ataque_elegido) - 1  # Convertir a entero y restar 1 para obtener el índice correcto
        else:
            print("Opción inválida, seleccione de nuevo...")


def calcular_velocidad(velocidad_ataque, velocidad_jugador):
    return (velocidad_jugador*velocidad_ataque)/2

def calcular_dano_inflingido(fuerza_ataque, fuerza_personaje):
    return int(((fuerza_ataque*1.5)/2)*(fuerza_personaje/2))

def probabilidad_esquivar(iq):
    probabilidad = iq*5
    nro = randint(1, 100)
    if nro < probabilidad:
        return True
    else:
        return False
def vivo_o_muerto (personaje1, personaje2):
    if personaje1.vida <= 0:
        print(f"\t\t\t{personaje1.nombre} se ha quedado sin vida :c\n"
              f"\t\t\t{personaje2.nombre} HA GANADO")
        sys.exit()





