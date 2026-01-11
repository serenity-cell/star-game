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
surface= pygame.Surface((100, 200))
surface.fill("red")
x = 100

#importing images
#importing player img
player_surface = pygame.image.load(join("images", "ship.png")).convert_alpha()
player_rect = player_surface.get_rect(center = (window_width/2, window_height/1.2))
#importing laser img
laser_surface = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = laser_surface.get_rect(center = (window_width/1.05, window_height/1.1) )
#importing meteor img
meteor_surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surface.get_rect(center = (window_width/2, window_height/2))
#importing stars img
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

    display.blit(meteor_surface, meteor_rect)
    display.blit(laser_surface, laser_rect)
    display.blit(player_surface, player_rect)

    pygame.display.update()

pygame.quit()


