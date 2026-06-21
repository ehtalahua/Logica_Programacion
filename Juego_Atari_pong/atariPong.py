import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO = 640
ALTO = 480
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atari Pong")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Variables del juego
bola_x = ANCHO // 2
bola_y = ALTO // 2
vel_x = 5
vel_y = 5

paleta_j = ALTO // 2 - 40
paleta_cpu = ALTO // 2 - 40
paleta_ancho = 10
paleta_alto = 80

puntos_j = 0
puntos_cpu = 0

# Fuente para marcador
fuente = pygame.font.SysFont("Arial", 30)

# Bucle principal
clock = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta_j > 0:
        paleta_j -= 7
    if teclas[pygame.K_s] and paleta_j < ALTO - paleta_alto:
        paleta_j += 7

    # Movimiento de la CPU (sigue la pelota)
    paleta_cpu = bola_y - paleta_alto // 2

    # Movimiento de la pelota
    bola_x += vel_x
    bola_y += vel_y

    # Rebote en paredes
    if bola_y <= 0 or bola_y >= ALTO:
        vel_y *= -1

    # Rebote en paleta jugador
    if bola_x <= 20 and paleta_j <= bola_y <= paleta_j + paleta_alto:
        vel_x *= -1

    # Rebote en paleta CPU
    if bola_x >= ANCHO - 20 and paleta_cpu <= bola_y <= paleta_cpu + paleta_alto:
        vel_x *= -1

    # Punto CPU
    if bola_x <= 0:
        puntos_cpu += 1
        bola_x, bola_y = ANCHO // 2, ALTO // 2
        vel_x *= -1

    # Punto jugador
    if bola_x >= ANCHO:
        puntos_j += 1
        bola_x, bola_y = ANCHO // 2, ALTO // 2
        vel_x *= -1

    # Dibujar elementos
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, BLANCO, (10, paleta_j, paleta_ancho, paleta_alto))
    pygame.draw.rect(ventana, BLANCO, (ANCHO - 20, paleta_cpu, paleta_ancho, paleta_alto))
    pygame.draw.circle(ventana, BLANCO, (bola_x, bola_y), 10)

    # Dibujar marcador
    texto = fuente.render(f"Jugador: {puntos_j}  CPU: {puntos_cpu}", True, BLANCO)
    ventana.blit(texto, (ANCHO//2 - texto.get_width()//2, 20))

    pygame.display.flip()
    clock.tick(60)
