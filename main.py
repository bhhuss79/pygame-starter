import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/forest-assets/door.png').convert()

# Load the spritesheet
spritesheet = pygame.image.load('assets/gfx/objects.png').convert()


# Create the first image
img = pygame.Surface([100,100]).convert()
img.blit(spritesheet, (0, 0), (0, 0, 16, 16))

# Create the second image
img = pygame.Surface([16, 16]).convert()
img.blit(spritesheet, (0, 0), (16, 0, 16, 16))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(img, (400, 300))
    win.blit(img, (100, 100))
    win.blit(img, (150, 100))
