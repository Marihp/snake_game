import random

import pygame
from pygame.math import Vector2


class Inicio:
    def __init__(self):
        pygame.init()

        # Reloj
        self.clock = pygame.time.Clock()

        # Tamaño de la celda y el numero de celdas
        self.cell_size = 40
        self.cell_number = 13
        # Colores
        self.verde_oscuro = (142, 204, 58)
        self.verde_claro = (167, 217, 73)
        self.azul = (79, 134, 198)

        # Crear la ventana
        self.ventana = pygame.display.set_mode(
            (
                self.cell_number * self.cell_size,
                self.cell_number * self.cell_size,
            )
        )
        # Titulo de la ventana
        pygame.display.set_caption("Snake Game")
        self.ventana.fill(self.verde_oscuro)

    def patron_tablero(self):
        """Patron de tablero de ajedrez en la ventana."""
        for row in range(self.cell_number):
            for col in range(self.cell_number):
                if (row + col) % 2 == 0:
                    cuadrado = pygame.Rect(
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    )
                    pygame.draw.rect(self.ventana, self.verde_claro, cuadrado)


class Game:
    pass


class Snake:
    pass


class Food:
    def __init__(self, cell_size=40):
        """Inicializar la comida.
        Trabaja con coordenadas en vectores.
        La posición toca multiplicarla por el tamaño de la celda.
        """
        # Crear coordenadas de inicio de la comida
        self.cell_size = cell_size
        self.x = 10 * cell_size
        self.y = 2 * cell_size
        self.posicion = Vector2(self.x, self.y)

    def dibujar_comida(self, surface):
        """Dibujar la comida en la ventana."""
        # Crear un rectangulo para la comida
        comida_rect = pygame.Rect(
            self.posicion.x, self.posicion.y, self.cell_size, self.cell_size
        )
        # Dibujar el rectangulo
        self.azul = (79, 134, 198)
        pygame.draw.rect(surface, self.azul, comida_rect)

    def randomize(self, posicion_serpiente):
        """Cambiar la posición de la comida de forma aleatoria."""
        self.x = random.randint(0, 12) * self.cell_size
        self.y = random.randint(0, 12) * self.cell_size

        # Verificar que la comida no se genere en la serpiente
        if Vector2(self.x, self.y) in posicion_serpiente:
            self.randomize(posicion_serpiente)
        else:
            self.posicion = Vector2(self.x, self.y)


if __name__ == "__main__":
    # Inicializar el juego
    inicio = Inicio()
    inicio.patron_tablero()

    # Dibujar la comida
    comida = Food()
    comida.dibujar_comida(inicio.ventana)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
