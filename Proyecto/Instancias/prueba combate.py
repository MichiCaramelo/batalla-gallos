class Combate:
    @staticmethod
    def calcular_velocidad(personaje):
        return (personaje.velocidad + personaje.ataque_actual.velocidad_ataque) / 2

    @staticmethod
    def calcular_daño(personaje):
        return ((personaje.ataque_actual.fuerza_ataque * 1.5) / 2) * personaje.fuerza

    @staticmethod
    def calcular_probabilidad_esquive(personaje):
        # Calcula la probabilidad de esquivar el ataque basado en el IQ
        return (personaje.iq * 2.5) / 100

    @staticmethod
    def combatir(jugador, enemigo):
        # Calcula la velocidad de cada personaje
        velocidad_jugador = Combate.calcular_velocidad(jugador)
        velocidad_enemigo = Combate.calcular_velocidad(enemigo)

        # Determina quién ataca primero basado en la velocidad
        if velocidad_jugador >= velocidad_enemigo:
            atacante = jugador
            defensor = enemigo
        else:
            atacante = enemigo
            defensor = jugador

        # Ataque del atacante al defensor
        print(f"{atacante.nombre} ataca a {defensor.nombre} con {atacante.ataque_actual.nombre_ataque}!")
        # Verifica si el defensor esquiva el ataque
        if Combate.calcular_probabilidad_esquive(defensor) < 0.5:  # 50% de probabilidad de esquivar
            print(f"{defensor.nombre} esquiva el ataque!")
        else:
            # Calcula el daño causado al defensor
            daño_causado = Combate.calcular_daño(atacante)
            print(f"{defensor.nombre} recibe {daño_causado} de daño!")
            # Resta la vida al defensor
            defensor.vida -= daño_causado
            # Verifica si el defensor queda fuera de combate
            if defensor.vida <= 0:
                print(f"{defensor.nombre} ha sido derrotado!")
                return True  # Devuelve True si el defensor ha sido derrotado

        return False  # Devuelve False si el combate continúa

# Ejemplo de uso:
# Supongamos que 'jugador' y 'enemigo' son instancias de las clases de personajes que van a pelear
# Combate.combatir(jugador, enemigo)