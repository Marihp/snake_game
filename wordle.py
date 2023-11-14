import flet as ft
from flet import *
from random_spanish_words import Word
from time import sleep
from unicodedata import normalize

ROWS = []


def store_row(function):
    def wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        ROWS.append(res)
        return res

    return wrapper


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
        # Obtener una palabra aleatoria
        word = Word().Find_Word_By().Len().Run(exact=self.increment_counter.counter)
        word = normalize("NFKD", word).encode("ASCII", "ignore").decode("ASCII")
        # Eliminar todos los controles actuales en la página
        self.page.clean()

        # Actualizar la página
        self.page.update()
        self.page.add(
            GameGrid(self.increment_counter.counter),
            GameInput(self.increment_counter.counter, word),
        )

    def build(self) -> Row:
        return Row(
            controls=[
                ElevatedButton(self.text, on_click=self.comenzar),
            ],
            alignment=MainAxisAlignment.CENTER,
            width=300,
        )


class GameInput(UserControl):
    def __init__(self, numero_letras: int, word: str):
        super().__init__()
        self.numero_letras = numero_letras
        self.word = word
        self.guesses_remaining = 6  # Número máximo de intentos
        self.current_line = 0
        print(self.word)

    def check_word(self, e: ControlEvent) -> None:
        entered_word = e.control.value
        print(entered_word)

        if len(entered_word) != self.numero_letras:
            print("La palabra debe tener {} letras.".format(self.numero_letras))
            return

        # Verificar si la palabra es correcta
        if entered_word == self.word:
            print("¡Ganaste!")

        elif self.current_line >= 5 or self.guesses_remaining <= 0:
            print("¡Perdiste!")

        else:
            # Actualizar la interfaz de usuario con los resultados de la adivinanza
            self.update_ui(entered_word)
            self.guesses_remaining -= 1
            self.current_line += 1

    def update_ui(self, entered_word: str) -> None:
        # Obtener la palabra objetivo como lista de caracteres
        target_word_list = tuple(self.word)
        target_word_set = set(target_word_list)

        # Inicializar la fila actual de la interfaz de usuario
        current_row = ROWS[self.current_line].controls

        for index, box in enumerate(current_row):
            box.content.value = entered_word[index].upper()
            box.content.offset = transform.Offset(0, 0)
            box.content.opacity = 1
            box.content.color = colors.WHITE

            if entered_word[index] in target_word_set:
                box.bgcolor = colors.ORANGE
                if entered_word[index] == target_word_list[index]:
                    box.bgcolor = colors.GREEN

            sleep(0.3)
            box.update()

    def build(self):
        hint_word = TextField(
            hint_text="Escribe una palabra",
            on_submit=self.check_word,
        )

        return Row(
            controls=[
                hint_word,
            ],
            alignment=MainAxisAlignment.CENTER,
            width=300,
        )


class GameError(UserControl):
    # Falta implementar
    def __init__(self):
        super().__init__()


class GameGrid(UserControl):
    def __init__(self, numero_letras: int):
        super().__init__()
        self.numero_letras = numero_letras

    @store_row
    def create_single_row(self):
        """
        Crea una fila de letras
        Eficiencia: O(n) donde n es el numero de letras
        """
        row = Row(alignment=MainAxisAlignment.CENTER)

        for i in range(self.numero_letras):
            row.controls.append(
                Container(
                    width=52,
                    height=52,
                    border=border.all(0.5, colors.WHITE24),
                    alignment=alignment.center,
                    clip_behavior=ClipBehavior.HARD_EDGE,
                    animate=animation.Animation(300, "decelerate"),
                    content=Text(
                        size=20,
                        weight="bold",
                        opacity=0,
                        offset=transform.Offset(0, 0.75),
                        animate_opacity=animation.Animation(300, "decelerate"),
                        animate_offset=animation.Animation(300, "decelerate"),
                    ),
                )
            )

        return row

    def build(self):
        """
        Crea un tablero de juego con el numero de letras indicado
        Eficiencia: O(1) porque siempre son 5 filas
        """
        Texto = Text("WORDLE", size=40, weight="bold")
        instrucciones = Text(
            "Escribe una palabra de {} letras".format(self.numero_letras),
            size=20,
            color="gray",
        )

        rows = [self.create_single_row() for _ in range(5)]

        return Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Row(controls=[Texto], alignment=MainAxisAlignment.CENTER),
                Row(controls=[instrucciones], alignment=MainAxisAlignment.CENTER),
                Divider(height=20, color=colors.TRANSPARENT),
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    controls=rows,
                ),
            ],
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
