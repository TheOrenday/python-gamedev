import pygame
pygame.init()
def cargar_record():
    try:
        with open("record.txt", "r") as archivo:
            return int(archivo.read())
    except (FileNotFoundError, ValueError):
        return 0
def guardar_record(record):
    with open("record.txt", "w") as archivo:
        archivo.write(str(record))
def reiniciar():
    return 100, 100, 100, 0, 700, 300, 3
pantalla = pygame.display.set_mode((800, 600))   # ancho, alto
pygame.display.set_caption("Mi primer juego")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 36)
fuente_grande = pygame.font.SysFont(None, 100)
x, y, vida, puntos, x_enemigo, y_enemigo, velocidad_enemigo = reiniciar()
record = cargar_record()
velocidad_jugador = 5
color_jugador = (255, 0, 0)
corriendo = True
game_over = False
while corriendo:
    # 1. Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    teclas = pygame.key.get_pressed()
    if game_over:
        if teclas[pygame.K_r]:
           x, y, vida, puntos, x_enemigo, y_enemigo, velocidad_enemigo = reiniciar()
           game_over = False
        if teclas[pygame.K_ESCAPE]:
            corriendo = False
    else:
    # 2. Actualizar (aquí irá la lógica)
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
        y_enemigo = y_enemigo + velocidad_enemigo
        if y_enemigo > 550 or y_enemigo < 0:
            velocidad_enemigo = -velocidad_enemigo
        if x_enemigo > x:
            x_enemigo = x_enemigo - 1
        elif x_enemigo < x:
            x_enemigo = x_enemigo + 1
        rect_jugador = pygame.Rect(x, y, 50, 50)
        rect_enemigo = pygame.Rect(x_enemigo, y_enemigo, 50, 50)
        if rect_jugador.colliderect(rect_enemigo):
            vida = vida - 50
            x = 100
            y = 100
            x_enemigo = 700
        if vida <= 0:
            vida = 0
            game_over = True
        puntos = puntos + 1
        if puntos > record:
            record = puntos
        if puntos > 0 and puntos % 300 == 0:
            if velocidad_enemigo > 0:
                velocidad_enemigo = velocidad_enemigo + 1
            else:
                velocidad_enemigo = velocidad_enemigo - 1
        # 3. Dibujar
    pantalla.fill((20, 20, 40))                  
    pygame.draw.rect(pantalla, color_jugador, (x, y, 50, 50))
    pygame.draw.rect(pantalla, (0, 0, 255), (x_enemigo, y_enemigo, 50, 50)) 
    texto = fuente.render(f"Vida: {vida}", True, (255, 255, 255))
    pantalla.blit(texto, (10,10))
    texto = fuente.render(f"Puntos: {puntos}", True, (255, 255, 255))
    pantalla.blit(texto, (10,40))
    if game_over:
        texto_fin = fuente_grande.render("GAME OVER", True, (255, 0, 0)) 
        pantalla.blit(texto_fin, (200, 250))
        texto_reinicio = fuente.render("R: para reiniciar | ESC: para salir", True, (255, 255, 255))
        pantalla.blit(texto_reinicio, (230, 340))
        
    texto = fuente.render(f"Record: {record}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 70)) 
    pygame.display.flip()                       
    reloj.tick(60)
guardar_record(record)                              
pygame.quit()