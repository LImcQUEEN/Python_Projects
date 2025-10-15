import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 800, 600
FPS = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Player variables
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5

# Item variables
item_size = 30
item_spawn_delay = 60  # number of frames between item spawns
item_spawn_timer = 0
items = []

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    # Item spawning
    if item_spawn_timer == 0:
        item_x = random.randint(0, WIDTH - item_size)
        item_y = random.randint(0, HEIGHT - item_size)
        items.append((item_x, item_y))
        item_spawn_timer = item_spawn_delay
    else:
        item_spawn_timer -= 1

    # Collision detection (player with items)
    for item in items[:]:
        item_rect = pygame.Rect(item[0], item[1], item_size, item_size)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        if player_rect.colliderect(item_rect):
            items.remove(item)

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))

    for item in items:
        pygame.draw.circle(screen, YELLOW, (item[0] + item_size // 2, item[1] + item_size // 2), item_size // 2)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
