import pygame
from os.path import join
from random import randint

#general setup
pygame.init
window_width, window_height = 1800, 1200
pygame.display.set_caption("asteroid game")
display = pygame.display.set_mode((window_width, window_height)) 
running = True
clock = pygame.time.Clock()

#creating the player surface
surface= pygame.Surface((100, 200))
surface.fill("red")
x = 100

#importing images
player_surface = pygame.image.load(join("images", "ship.png")).convert_alpha()
player_rect = player_surface.get_frect(center = (window_width/2, window_height/1.2))
player_direction = pygame.math.Vector2
player_surface= pygame.transform.scale(player_surface, (100, 200))
player_speed = 300 

laser_surface = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = laser_surface.get_frect(center = (window_width/1.05, window_height/1.1) )

meteor_surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (window_width/2, window_height/1))


star_surface = pygame.image.load(join("images", "stars.png")).convert_alpha()
star_potisions =[(randint(0, window_width), randint(0, window_height)) for i in range(20)]


"""def player_movement(window_width, player_rect):
    keys = pygame.key.get_pressed()
    if player_rect.right < window_width and player_rect.left > 0:
        if keys[pygame.K_LEFT]:
            player_rect.left -= 5
            print("going left")

        elif keys[pygame.K_RIGHT]:
            player_rect.left +=  5
            print("going right")
            
    elif player_rect.right < window_width:
        player_rect.left += 5
    
    elif player_rect.left > 0:
        player_rect.left -= 5  """

#player movement like a dvd player 
dir_x, dir_y = 2 , 2
def dvd_bounce(dir_x, dir_y):
    if player_rect.right < window_width and player_rect.left > 0 and player_rect.top < window_height and player_rect.bottom > 0:
        player_rect.center += player_direction(dir_x, dir_y) * player_speed * dt

    elif player_rect.top < 0 or player_rect.bottom > window_height:      
        player_rect.bottom -= 5
        player_rect.center += player_direction(dir_x, -dir_y) * player_speed * dt

    elif player_rect.right > window_width and player_rect.left < 0:
        player_rect.center += player_direction(-dir_x, dir_y) * player_speed * dt
        

#-- MAIN LOOP --
while running:
    #dynamic fps handling
    dt = clock.tick(60) / 10000

    print(player_rect.bottom > window_height or player_rect.top < 0 )
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

    #player moevement
    player_surface.fill("orange")
    display.blit(player_surface, player_rect)
    dvd_bounce(dir_x, dir_y)

    pygame.display.update()

pygame.quit()


