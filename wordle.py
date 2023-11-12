import flet as ft
from flet import *


class IncrementCounter(UserControl):
    """Un control que muestra un texto y un botón para incrementar un contador."""

    def __init__(self, text: str, start_number: int = 0) -> None:
        """Inicializa el control con el texto y el número inicial.
        Eficiencia: O(1)
        """
        super().__init__()
        self.text = text
        self.counter = start_number
        self.text_number: Text = Text(value=str(start_number), size=40)

    def increment(self, e: ControlEvent) -> None:
        """Incrementa el contador y actualiza el texto.
        Eficiencia: O(1)
        """
        if self.counter < 8:
            self.counter += 1
            self.text_number.value = str(self.counter)
            self.update()

    def build(self) -> Row:
        """Construye el control.
        Eficiencia: O(1)
        """
        return Row(
            controls=[
                ElevatedButton(self.text, on_click=self.increment),
                self.text_number,
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            width=300,
        )


class botonComenzar(UserControl):
    def __init__(
        self, text: str, increment_counter: IncrementCounter, page: Page
    ) -> None:
        super().__init__()
        self.text = text
        self.increment_counter = increment_counter
        self.page = page

    # Crear el tablero de juego
    def comenzar(self, e: ControlEvent) -> None:
        # Eliminar todos los controles actuales en la página
        self.page.clean()

        # Agregar un nuevo control de texto con el mensaje de inicio del juego
        self.page.add(Text("¡Que comience el juego!", size=40))

        # Actualizar la página
        self.page.update()

    def build(self) -> Row:
        return Row(
            controls=[
                ElevatedButton(self.text, on_click=self.comenzar),
            ],
            alignment=MainAxisAlignment.CENTER,
            width=300,
        )


def main(page: Page) -> None:
    page.title = "Wordle the game"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    increment_counter = IncrementCounter("# de letras", start_number=4)
    boton_comenzar = botonComenzar("Comenzar", increment_counter, page)

    page.add(
        Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text("WORDLE", size=40, weight="bold"),
                    ],
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text("El juego de adivinar palabras", size=20, color="gray"),
                    ],
                ),
                Divider(height=20, color=colors.TRANSPARENT),
                # Boton para incrementar el numero de letras
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        increment_counter,
                    ],
                ),
                # Boton para comenzar el juego
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        boton_comenzar,
                    ],
                ),
            ],
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
