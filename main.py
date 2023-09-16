import pygame


class Inicio:
    def __init__(self):
        pygame.init()
        self.cell_size = 40
        self.cell_number = 13
        self.verde_oscuro = (142, 204, 58)
        self.verde_claro = (167, 217, 73)
        self.azul = (79, 134, 198)
        self.ventana = pygame.display.set_mode(
            (
                self.cell_number * self.cell_size,
                self.cell_number * self.cell_size,
            )
        )
        pygame.display.set_caption("Snake Game")
        self.ventana.fill(self.verde_oscuro)

    def patron_tablero(self):
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
    pass


if __name__ == "__main__":
    inicio = Inicio()
    inicio.patron_tablero()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
