import os
import pygame

import config

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

        # Pinto el fondo con el color elegido (bg)
        self.screen.fill(config.COLOR_FONT)

    def draw_entity(self, entity):
        poly = [
            (int(entity.position.x * WIDTH_CELL), int(entity.position.y * HEIGHT_CELL)),
            (int((entity.position.x + 1) * WIDTH_CELL), int(entity.position.y * HEIGHT_CELL)),
            (int((entity.position.x + 1) * WIDTH_CELL), int((entity.position.y + 1) * HEIGHT_CELL)),
            (int(entity.position.x * WIDTH_CELL), int((entity.position.y + 1) * HEIGHT_CELL)),
        ]
        pygame.draw.polygon(self.screen, entity.color, poly, 0)

    def print_window(self, land):
        # Recorro cada una de las celdas generadas
        for y in range(0, self.width):
            for x in range(0, self.height):
                entity = land.getMostVisibleCreature(x, y)
                if entity:
                    self.draw_entity(entity)
                else:
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

    @staticmethod
    def wait(miliseconds):
        pygame.time.wait(miliseconds)
