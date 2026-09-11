
import pygame
import random

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Runner")

# Colors
GREEN = (40, 160, 80)
BLUE = (50, 150, 255)
RED = (220, 50, 50)
YELLOW = (255, 220, 40)
WHITE = (255, 255, 255)

# Player
player = pygame.Rect(100, 400, 40, 40)
speed = 5

# Treasure
treasure = pygame.Rect(
    random.randint(200, 750),
    random.randint(100, 400),
    25,
    25
)

# Obstacle
obstacle = pygame.Rect(700, 400, 40, 40)
obstacle_speed = 5

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]: