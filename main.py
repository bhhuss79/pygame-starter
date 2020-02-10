import pygame # import library
pygame.init()

img = pygame.image.load('sprite.png').convert 
img = pygame.image.load("assets/gfx/log.png").convert()
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
  pygame.display.update()

print("Ending game")
pygame.quit()

