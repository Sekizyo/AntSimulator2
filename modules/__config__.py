import pygame

WIDTH = 800 #  - Screen width
HEIGHT = 800 #  - Screen height

BLOCKSIZE = 50 #  - Scale block size, it greatly influences prerformance. Optimal values: 8 - 25
FPS = 5

WIDTHBLOCKS = WIDTH//BLOCKSIZE
HEIGHTBLOCKS = HEIGHT//BLOCKSIZE

TRAILEXPIRATIONRATE = 1

FONT = pygame.font.SysFont("Arial", 18)