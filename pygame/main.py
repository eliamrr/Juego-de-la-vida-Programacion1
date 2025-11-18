import pygame

ANCHO = 800
ALTO = 600

ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Juego de la vida")


iniciar = True
#Color paantalla
BLANCO = (255, 255, 255)
VERDE = (0,255,0)


ventana.fill(BLANCO)

pygame.draw.rect(ventana, VERDE,(0,100,600,200))

while iniciar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            iniciar = False
    pygame.display.update()
pygame.quit()

