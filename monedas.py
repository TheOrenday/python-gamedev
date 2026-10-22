import pygame
import random
pygame.init()
def crear_moneda():
    mx = random.randint(0, 770)
    my = random.randint(0, 570)
    return pygame.Rect(mx, my, 30, 30)
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("MONEDAS")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 36)
fuente_grande = pygame.font.SysFont(None, 100)
monedas = []
for i in range(5):
    monedas.append(crear_moneda())
corriendo = True
game_over = False
x = 100
y = 100
puntos = 0
velocidad_jugador = 3
while corriendo:
    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        x = x + velocidad_jugador
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        x = x - velocidad_jugador
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        y = y - velocidad_jugador
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        y = y + velocidad_jugador
    if x > 750:
        x = 750
    elif x < 0:
        x = 0
    if y > 550:
        y = 550
    elif y < 0:
        y = 0
    rect_jugador = pygame.Rect(x, y, 50, 50)
    for moneda in monedas[:]:
        if rect_jugador.colliderect(moneda):
            monedas.remove(moneda)
            puntos = puntos + 1
            monedas.append(crear_moneda())
    pantalla.fill((20, 20, 40))
    texto = fuente.render(f"Puntos: {puntos}", True, (255, 255, 255))
    pygame.draw.rect(pantalla, (255, 0, 0), rect_jugador)
    for moneda in monedas:
        pygame.draw.rect(pantalla, (255, 215, 0), moneda)
    pantalla.blit(texto, (10, 10))
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()