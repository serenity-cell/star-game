import pygame
from os.path import join
from random import randint

#general setup
pygame.init
window_width, window_height = 1800, 1200
pygame.display.set_caption("asteroid game")
display = pygame.display.set_mode((window_width, window_height)) 
running = True

#creating the player surface
surface= pygame.Surface((100,200))
surface.fill("red")
x = 100

#importing images
player_surface = pygame.image.load(join("images", "starship.jpeg")).convert()
star_surface = pygame.image.load(join("images", "stars.png")).convert_alpha()
star_potisions =[(randint(0, window_width), randint(0, window_height)) for i in range(20)]

#--main loop --
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    


    #draw the game
    display.fill("darkblue")
    for pos in star_potisions:
        display.blit(star_surface, pos)
    x += 0.1
    display.blit(player_surface, (x,700))
    
    pygame.display.update()

pygame.quit()


