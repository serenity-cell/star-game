import pygame
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image: pygame.Surface = pygame.image.load(join("images", "ship.png")).convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(center = (window_width/2, window_height/1.2))
    
    def movement(self, dt):
        self.direction = pygame.math.Vector2()
        self.speed = 300 
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction.x= int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        if pygame.key.get_just_pressed()[pygame.K_SPACE]:
            print("fire laser")
    
    
    def dvd_movement(self, func_y, func_x):
        if self.rect.top < 0 or self.rect.bottom > window_height:      
          func_y = func_y * -1

        elif self.rect.right > window_width or self.rect.left < 0:
         func_x = func_x * -1

        return func_x, func_y

#general setup up layer_surface
pygame.init
window_width, window_height = 1800, 1200
pygame.display.set_caption("asteroid game")
display = pygame.display.set_mode((window_width, window_height)) 
running = True
clock = pygame.time.Clock()

#creating the player surface
surface= pygame.Surface((100, 200))
x = 100

all_sprites = pygame.sprite.Group()
player =  Player(all_sprites)



#importing images

laser_surface: pygame.Surface = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect: pygame.FRect = laser_surface.get_frect(center = (window_width/1.05, window_height/1.1) )

meteor_surface: pygame.Surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect: pygame.FRect = meteor_surface.get_frect(center = (window_width/2, window_height/1))

star_surface: pygame.Surface = pygame.image.load(join("images", "stars.png")).convert_alpha()
star_positions =[(randint(0, window_width), randint(0, window_height)) for i in range(20)]

#player movement like a dvd player 
'''dir_x, dir_y = 1.5 , 1.5
def dvd_bounce(func_x , func_y):
    if player_rect.top < 0 or player_rect.bottom > window_height:      
        func_y = func_y * -1

    elif player_rect.right > window_width or player_rect.left < 0:
        func_x = func_x * -1

    return func_x, func_y'''
        

#-- MAIN LOOP --
while running:
    #dynamic fps handling
    dt = clock.tick(60) / 1000

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    

    all_sprites.update(dt)

    #draw the game
    display.fill("darkblue")
    for pos in star_positions:
        display.blit(star_surface, pos)


    #display.blit(meteor_surface, meteor_rect)
    #display.blit(laser_surface, laser_rect)
    all_sprites.draw(display)
    

    pygame.display.update()

pygame.quit()


