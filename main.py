import random
import pygame
from collections import deque
from itertools import islice
from pygame.math import Vector2

# Inicialización de Pygame
pygame.init()

# Tamaño de la celda y el número de celdas en el tablero
tamaño_celda = 40
numero_celdas = 13
posibles_posiciones = deque([Vector2(x, y) for x in range(
    numero_celdas) for y in range(numero_celdas)])

# Definición de colores utilizados en el juego
verde_oscuro = (142, 204, 58)
verde_claro = (167, 217, 73)
azul = (79, 134, 198)
blanco = (255, 255, 255)
rojo = (255, 0, 0)

# Direcciones posibles para la serpiente
ARRIBA = Vector2(0, -1)
ABAJO = Vector2(0, 1)
IZQUIERDA = Vector2(-1, 0)
DERECHA = Vector2(1, 0)


class Serpiente:
    def __init__(self):
        """Inicializa la serpiente.

        La serpiente se representa como una lista de vectores, donde cada
        vector representa un segmento del cuerpo. El primer elemento de la
        lista es la cabeza de la serpiente.

        - Eficiencia: O(1) ya que el tamaño de la serpiente es constante.
        """
        self.cuerpo = deque([Vector2(4, 4), Vector2(4, 5), Vector2(3, 5)])
        self.ultima_cola = Vector2(3, 5)
        self.direccion = ARRIBA
        self.nueva_parte = False

    def mover(self):
        """Mueve la serpiente.

        La serpiente se mueve insertando una nueva cabeza en la dirección
        actual y eliminando la cola.

        - Eficiencia: O(1) ya que se inserta y elimina elementos de la lista
          siempre en los extremos.
        """
        if not self.nueva_parte:
            self.ultima_cola = self.cuerpo.pop()
        else:
            self.nueva_parte = False

        nueva_cabeza = self.cuerpo[0] + self.direccion
        self.cuerpo.appendleft(nueva_cabeza)

    def colision_pared(self):
        """Verifica si la serpiente chocó con la pared.

        Comprueba si la cabeza de la serpiente está fuera de los límites del
        tablero.

        - Eficiencia: O(1) ya que se accede a los elementos de la lista por
          índice.
        """
        cabeza = self.cuerpo[0]
        return (
            cabeza.x < 0
            or cabeza.x >= numero_celdas
            or cabeza.y < 0
            or cabeza.y >= numero_celdas
        )

    def colision_cuerpo(self):
        """Verifica si la serpiente chocó con su propio cuerpo.

        Comprueba si la cabeza de la serpiente está en el cuerpo.

        - Eficiencia: O(n) ya que se recorre la lista de la serpiente.
        """
        return self.cuerpo[0] in islice(self.cuerpo, 1, None)

    def comer(self, comida):
        """Verifica si la serpiente ha comido la comida.

        Comprueba si la cabeza de la serpiente está en la posición de la
        comida y actualiza la posición de la comida de ser necesario.

        - Eficiencia: O(1) ya que se accede a los elementos de la lista por
          índice.
        """
        if self.cuerpo[0] == comida.posicion:
            comida.posicion = comida.posicion_aleatoria(self.cuerpo)
            self.nueva_parte = True


class Comida:
    def __init__(self):
        """Inicializa la comida."""
        # Posición inicial de la comida
        self.posicion = Vector2(10, 2)

    def posicion_aleatoria(self, no_permitidos):
        """Retorna un Vector2 con una posición aleatoria que no está en el
        cuerpo de la serpiente.

        - Eficiencia: O(n) donde n es el tamaño del tablero, aunque en este
          caso es O(1) ya que el tablero tiene un tamaño fijo.
        """
        def diferencia_entre_deques(deque1, deque2):
            # Crea un deque vacío para almacenar el resultado
            resultado = deque()

            # Convierte el deque2 en una lista para acelerar la búsqueda
            lista_deque2 = list(deque2)

            # Itera a través de los elementos en el deque1
            for elemento in deque1:
                # Verifica si el elemento no está en deque2
                if elemento not in lista_deque2:
                    resultado.append(elemento)

            return resultado

        lista_posibles = diferencia_entre_deques(
            posibles_posiciones, no_permitidos)
        return random.choice(lista_posibles)


class Tablero:
    def __init__(self, serpiente):
        """Inicia el tablero del juego con una serpiente y una cuadrícula."""
        self.pantalla = pygame.display.set_mode(
            (numero_celdas * tamaño_celda, numero_celdas * tamaño_celda)
        )
        pygame.display.set_caption("Juego de la Serpiente")
        self.font = pygame.font.Font(None, 36)
        # Creamos el patrón de cuadrícula
        self.patron = self.generar_patron_tablero()
        self.pantalla.blit(self.patron, (0, 0))
        # Dibujamos la serpiente inicialmente
        for segmento in serpiente.cuerpo:
            serpiente_rect = pygame.Rect(
                segmento.x * tamaño_celda,
                segmento.y * tamaño_celda,
                tamaño_celda,
                tamaño_celda,
            )
            pygame.draw.rect(self.pantalla, rojo, serpiente_rect)

    def generar_patron_tablero(self):
        """Crea una cuadrícula en la pantalla."""
        patron = pygame.Surface(self.pantalla.get_size())
        patron.fill(verde_oscuro)  # Llena con el color de fondo oscuro
        for fila in range(numero_celdas):
            for columna in range(numero_celdas):
                if (fila + columna) % 2 == 0:
                    cuadrado = pygame.Rect(
                        columna * tamaño_celda,
                        fila * tamaño_celda,
                        tamaño_celda,
                        tamaño_celda,
                    )
                    pygame.draw.rect(patron, verde_claro, cuadrado)
        return patron

    def actualizar_pantalla(self, serpiente, comida, perdio):
        """Refresca la pantalla del juego.

        - Eficiencia: O(1) ya que solo actualiza la cola y la cabeza en cada
          iteración.
        """
        comida_rect = pygame.Rect(
            comida.posicion.x * tamaño_celda,
            comida.posicion.y * tamaño_celda,
            tamaño_celda,
            tamaño_celda,
        )
        pygame.draw.rect(self.pantalla, azul, comida_rect)

        # Borramos la cola
        if not serpiente.nueva_parte:
            cola_rect = pygame.Rect(
                serpiente.ultima_cola.x * tamaño_celda,
                serpiente.ultima_cola.y * tamaño_celda,
                tamaño_celda,
                tamaño_celda,
            )
            if (serpiente.ultima_cola.y + serpiente.ultima_cola.x) % 2 == 0:
                pygame.draw.rect(self.pantalla, verde_claro, cola_rect)
            else:
                pygame.draw.rect(self.pantalla, verde_oscuro, cola_rect)

        # Dibujamos la cabeza
        cabeza_rect = pygame.Rect(
            serpiente.cuerpo[0].x * tamaño_celda,
            serpiente.cuerpo[0].y * tamaño_celda,
            tamaño_celda,
            tamaño_celda,
        )
        pygame.draw.rect(self.pantalla, rojo, cabeza_rect)

        if perdio:
            mensaje = self.font.render(
                "¡Perdiste! Presiona R para reiniciar.", True, blanco
            )
            mensaje_rect = mensaje.get_rect(
                center=(
                    self.pantalla.get_width() // 2,
                    self.pantalla.get_height() // 2,
                )
            )
            self.pantalla.blit(mensaje, mensaje_rect)

        pygame.display.flip()


def main():
    serpiente = Serpiente()
    tablero = Tablero(serpiente)
    comida = Comida()
    jugando = True
    perdio = False
    reloj = pygame.time.Clock()

    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    # Reiniciar el juego
                    serpiente = Serpiente()
                    comida = Comida()
                    tablero.pantalla.blit(tablero.patron, (0, 0))
                    perdio = False

        if not perdio:
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_UP] and serpiente.direccion != ABAJO:
                serpiente.direccion = ARRIBA
            elif teclas[pygame.K_DOWN] and serpiente.direccion != ARRIBA:
                serpiente.direccion = ABAJO
            elif teclas[pygame.K_LEFT] and serpiente.direccion != DERECHA:
                serpiente.direccion = IZQUIERDA
            elif teclas[pygame.K_RIGHT] and serpiente.direccion != IZQUIERDA:
                serpiente.direccion = DERECHA

            serpiente.mover()

            if serpiente.colision_pared() or serpiente.colision_cuerpo():
                perdio = True

            serpiente.comer(comida)

        tablero.actualizar_pantalla(serpiente, comida, perdio)
        reloj.tick(9)

    pygame.quit()


if __name__ == "__main__":
    main()
