import pygame
from recursos import colores

# Inicializamos Pygame
pygame.init()

# Creamos la ventana principal
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Titulo
pygame.display.set_caption("Juego de la vida")

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    pantalla.fill((colores.BANANA))
    pygame.display.update()




