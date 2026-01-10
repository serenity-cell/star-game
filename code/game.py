import pygame

#general setup
pygame.init
window_width, window_height = 1800, 1200
pygame.display.set_caption("asteroid game")
display = pygame.display.set_mode((window_width, window_height)) 

running = True

surface= pygame.Surface((100,200))
surface.fill("red")
x = 100
#importing images
player_surface = pygame.image.load("images/download(1).jpeg")
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #draw the game
    display.fill("darkblue")
    x += 0.1
    display.blit(surface, (x,700))

    pygame.display.update()

pygame.quit()


