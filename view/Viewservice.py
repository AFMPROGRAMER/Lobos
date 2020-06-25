import os
import time

import pygame

# Alto y ancho por celda
WIDTH_CELL = 10
HEIGHT_CELL = 10


class ViewService:
    # Alto y ancho en numero de celdas
    width = 0
    height = 0

    # Alto y ancho de la ventana en pixeles
    widthWindow = 0
    heightWindow = 0

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.widthWindow = width * WIDTH_CELL
        self.heightWindow = height * HEIGHT_CELL

        # Hago que la ventana aparezca centrada en Windows
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        pygame.init()

        # Establezco el título de la ventana:
        pygame.display.set_caption("Lobos y Ovejas. v0.1")

        # Creación de la ventana
        self.screen = pygame.display.set_mode((self.heightWindow, self.widthWindow))

        bg = 25, 25, 25
        # Pinto el fondo con el color elegido (bg)
        self.screen.fill(bg)

    def draw_entity(self, entity):
        # TODO
        pass
        # pygame.draw.polygon(self.screen, (128, 128, 128), poly, 1)

    def print_window(self):
        # Recorro cada una de las celdas generadas
        for y in range(0, self.width):
            for x in range(0, self.height):
                self.draw_poly(x, y)
        # Muestro y actualizo los fotogramas en cada iteración del bucle principal
        pygame.display.flip()

    def draw_poly(self, x, y):
        # Creación del polígono de cada celda a dibujar
        poly = [
            (int(x * WIDTH_CELL), int(y * HEIGHT_CELL)),
            (int((x + 1) * WIDTH_CELL), int(y * HEIGHT_CELL)),
            (int((x + 1) * WIDTH_CELL), int((y + 1) * HEIGHT_CELL)),
            (int(x * WIDTH_CELL), int((y + 1) * HEIGHT_CELL)),
        ]

        pygame.draw.polygon(self.screen, (128, 128, 128), poly, 1)


vs = ViewService(60, 60)
# Agrego pequeña pausa para que el cpu no trabaje al 100%
i = 0
while i < 10000:
    vs.print_window()
    i = i + 1
