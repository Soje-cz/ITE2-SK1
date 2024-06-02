import pygame

# Inicializace Pygame
pygame.init()

# Nastavení okna
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Ninja Animation")

# Načtení spritů pro chůzi do prava
walkRight = [pygame.image.load(f'{i}.png') for i in range(1, 8)]

# Načtení spritů pro chůzi do leva
# Obrázky jsou pojmenované 1.png až 7.png, není potřeba je překlápět
walkLeft = [pygame.transform.flip(img, True, False) for img in walkRight]

# Pozice postavy a proměnné pro animaci
x, y = 50, 50
width, height = 64, 64  # Předpokládá se velik
# ost sprite
velocity = 10
walkCount = 0
last_direction = 'right'  # Uložení poslední směru pohybu

# Hlavní herní smyčka
running = True
while running:
    pygame.time.delay(30)  # Zpomalení smyčky pro viditelnou animaci

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Získání stisknutých kláves
    keys = pygame.key.get_pressed()

    # Animace chůze do prava
    if keys[pygame.K_RIGHT]:
        x += velocity
        walkCount += 1
        last_direction = 'right'
    # Animace chůze do leva
    elif keys[pygame.K_LEFT]:
        x -= velocity
        walkCount += 1
        last_direction = 'left'
    else:
        walkCount = 0

    # Pokud dojdou sprity, začneme od prvního znovu
    if walkCount >= 7 * 3:  # 9 snímků, pomnožené třikrát pro zpomalení animace
        walkCount = 3

    # Update herního okna
    window.fill((255, 255, 255))  # Vyčistí okno (nastaví bílé pozadí)

    if last_direction == 'left':
        current_sprite = walkLeft[walkCount // 3]  # Dělení třemi pro zpomalení animace
    else:
        current_sprite = walkRight[walkCount // 3]  # Dělení třemi pro zpomalení animace

    window.blit(current_sprite, (x, y))

    pygame.display.update()

    # Nastavení FPS
    clock = pygame.time.Clock()
    clock.tick(120)

pygame.quit()
