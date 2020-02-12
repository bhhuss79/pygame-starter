import pygame # import library
pygame.init()

# Create the window
win = pygame.display.set_mode((1000, 1000))

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

# Game code starts here ---------------------
  win.fill((0, 0, 0))
 
  # Draw a rectangle
  pygame.draw.rect(win, (0, 204, 255), (50, 50, 100, 200))
  
  #Update the display
img = pygame.image.load("cave.png").convert 
img = pygame.image.load("assets/gfx/cave.png").convert()
print 
img = pygame.image.load("character.png").convert
img = pygame.image.load("assets/gfx/character.png").convert()
print
img = pygame.image.load("front.png").convert
img = pygame.image.load("assets/gfx/front.png").convert()
print 
img = pygame.image.load("Inner.png").convert
img = pygame.image.load("assets/gfx/Inner.png").convert()
print 
img = pygame.image.load("Log.png").convert
img = pygame.image.load("assets/gfx/Log.png").convert()
pygame.display.update()


print("Ending game")
