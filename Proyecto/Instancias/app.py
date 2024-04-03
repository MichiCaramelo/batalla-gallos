from clases.Personajes import *
from mecanicas import *
from random import randint
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H\033[J")
def mostrar_inicio():
    print("""BIENVENIDOS A LA BATALLA DE GALLOS
            1. Iniciar Partida
            2. Salir del programa""")
    while True:
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            iniciar_partida()
        elif opcion == "2":
            finalizar_ejecucion()
        else:
            print("Opcion invalida, ingresela nuevamente...")

def iniciar_partida():
    clear_screen()
    while True:
        print(f"""MENU DE PERSONAJES:
            1. Gallo Fortachon : {gallo_fortachon_instancia.descripcion}
            2. Gallo Volador: {gallo_volador_instancia.descripcion}
            3. Gallo Sabio: {gallo_sabio_instancia.descripcion}
            4. Gallina: {gallina_instancia.descripcion}
            5. Volver al inicio """)
        opcion = input("Elija para saber mas: ")
        if opcion == "1":
            gallo_fortachon_instancia.mostrar_info()
            jugador = gallo_fortachon_instancia
            elegir_personaje(jugador)
        elif opcion == "2":
            gallo_volador_instancia.mostrar_info()
            jugador = gallo_volador_instancia
            elegir_personaje(jugador)
        elif opcion == "3":
            gallo_sabio_instancia.mostrar_info()
            jugador = gallo_sabio_instancia
            elegir_personaje(jugador)
        elif opcion == "4":
            gallina_instancia.mostrar_info()
            jugador = gallina_instancia
            elegir_personaje(jugador)
        elif opcion == "5":
            mostrar_inicio()
        else:
            print("Opcion invalida, ingresela de nuevo...")
            clear_screen()

def finalizar_ejecucion():
    print ("\nSaliendo del programa...")
    sys.exit()

def elegir_personaje(jugador):
    clear_screen()
    while True:
        opcion = input("¿Desea elegir este personaje? (si/no)\n")
        if opcion.lower() == "si":
            enemigo = jugador
            while enemigo == jugador:
                nro_enemigo = randint(1, 4)
                if nro_enemigo == 1:
                    enemigo = gallo_fortachon_instancia
                elif nro_enemigo == 2:
                    enemigo = gallo_volador_instancia
                elif nro_enemigo == 3:
                    enemigo = gallo_sabio_instancia
                else:
                    enemigo = gallina_instancia
            combate(jugador, enemigo)

        elif opcion.lower() == "no":
            iniciar_partida()

        else:
            print("Ingrese una opcion correcta...")

def combate (jugador, enemigo):
    clear_screen()
    print (f"""\t\t\t\tEL COMBATE EMPIEZA
            {jugador.nombre} VS. {enemigo.nombre}""")

    while jugador.vida > 0 and enemigo.vida > 0:
        clear_screen()
        print(f"""\t\t\t\tVIDA ACTUAL
            JUGADOR (tú): {jugador.nombre} = {jugador.vida}
            ENEMIGO : {enemigo.nombre} = {enemigo.vida}\n""")

        # CALCULOS JUGADOR
        nro_ataque_elegido = elegir_ataque(jugador.ataques)
        ataque_elegido_jugador = jugador.ataques[nro_ataque_elegido]
        velocidad_jugador = calcular_velocidad(ataque_elegido_jugador.velocidad, jugador.velocidad)
        probabilidad_jugador = probabilidad_esquivar(jugador.iq)
        dano_inflingido_jugador = calcular_dano_inflingido(ataque_elegido_jugador.fuerza, jugador.fuerza)

        #CALCULOS ENEMIGO
        nro_ataque_elegido = randint(0, len(enemigo.ataques) - 1)
        ataque_elegido_enemigo = enemigo.ataques[nro_ataque_elegido]
        velocidad_enemigo = calcular_velocidad(ataque_elegido_enemigo.velocidad, enemigo.velocidad)
        probabilidad_enemigo = probabilidad_esquivar(enemigo.iq)
        dano_inflingido_enemigo = calcular_dano_inflingido(ataque_elegido_enemigo.fuerza, enemigo.fuerza)

        if velocidad_enemigo >= velocidad_jugador:
            print(f"\n{enemigo.nombre} ataca con {ataque_elegido_enemigo.nombre} a {jugador.nombre}")
            if probabilidad_jugador == True:
                print("El jugador a esquivado el ataque...")
                print(f"\n{jugador.nombre} ataca con {ataque_elegido_jugador.nombre} a {enemigo.nombre}")
                if probabilidad_enemigo == True:
                    print("El enemigo a esquivado el ataque")
                else:
                    print(f"{enemigo.nombre} pierde {dano_inflingido_jugador} de vida")
                    enemigo.vida = enemigo.vida - dano_inflingido_jugador
                    vivo_o_muerto(enemigo, jugador)
            else:
                print(f"{jugador.nombre} pierde {dano_inflingido_enemigo} de vida")
                jugador.vida = jugador.vida - dano_inflingido_enemigo
                vivo_o_muerto(jugador, enemigo)
                print(f"\n{jugador.nombre} ataca con {ataque_elegido_jugador.nombre} a {enemigo.nombre}")
                if probabilidad_enemigo == True:
                    print("El enemigo a esquivado el ataque")
                else:
                    print(f"{enemigo.nombre} pierde {dano_inflingido_jugador} de vida")
                    enemigo.vida = enemigo.vida - dano_inflingido_jugador
                    vivo_o_muerto(enemigo,jugador)
        else:
            print(f"\n{jugador.nombre} ataca con {ataque_elegido_jugador.nombre} a {enemigo.nombre}")
            if probabilidad_enemigo == True:
                print("El enemigo a esquivado el ataque")
                print(f"\n{enemigo.nombre} ataca con {ataque_elegido_enemigo.nombre} a {jugador.nombre}")
                if probabilidad_jugador == True:
                    print("El jugador a esquivado el ataque...")
                else:
                    print(f"{jugador.nombre} pierde {dano_inflingido_enemigo} de vida")
                    jugador.vida = jugador.vida - dano_inflingido_enemigo
                    vivo_o_muerto(jugador, enemigo)
            else:
                print(f"{enemigo.nombre} pierde {dano_inflingido_jugador} de vida")
                enemigo.vida = enemigo.vida - dano_inflingido_jugador
                vivo_o_muerto(enemigo, jugador)
                print(f"\n{enemigo.nombre} ataca con {ataque_elegido_enemigo.nombre} a {jugador.nombre}")
                if probabilidad_jugador == True:
                    print("El jugador a esquivado el ataque...")
                else:
                    print(f"{jugador.nombre} pierde {dano_inflingido_enemigo} de vida")
                    jugador.vida = jugador.vida - dano_inflingido_enemigo
                    vivo_o_muerto(jugador, enemigo)

    sys.exit()

gallo_fortachon_instancia = gallo_fortachon()
jugador = gallo_fortachon_instancia
gallo_volador_instancia = gallo_volador()
gallo_sabio_instancia = gallo_sabio()
gallina_instancia = gallina()
mostrar_inicio()

