import pygame
from os.path import join
from random import randint, uniform

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image: pygame.Surface = pygame.image.load(join("images", "ship.png")).convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(center = (window_width/2, window_height/1.2))
        self.direction = pygame.math.Vector2()
        self.speed = 500
        
        #cooldown
        self.can_shoot = True
        self.shoot_time = 0
        self.cooldown = 400
    
    def laser_timer(self):
        if not self.can_shoot:
            time = pygame.time.get_ticks()
            if time - self.shoot_time >= self.cooldown:
                self.can_shoot = True
        
    def update(self, dt):

        #player movement
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction.x= int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction = self.direction.normalize() if self.direction else self.direction

        # window restriction
        if self.rect.top <= 0 or self.rect.bottom >= window_height:
            self.direction.y = (int(keys[pygame.K_UP]) - int(keys[pygame.K_DOWN])) * 2
        elif self.rect.left <= 0 or self.rect.right >= window_width:
            self.direction.x= int(keys[pygame.K_LEFT]) - int(keys[pygame.K_RIGHT]) 

        self.rect.center += self.direction * self.speed * dt

        #laser shot
        if pygame.key.get_just_pressed()[pygame.K_SPACE] and self.can_shoot:
            Laser(self.rect.midbottom, laser_surf, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
        
        self.laser_timer()
        
    #dvd movement for player: inactive
    dir_x, dir_y = 1.5 , 1.5
    def dvd_movement(self, func_y, func_x):
        if self.rect.top < 0 or self.rect.bottom > window_height:      
          func_y = func_y * -1

        elif self.rect.right > window_width or self.rect.left < 0:
         func_x = func_x * -1

        return func_x, func_y        

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
    
    def update(self, dt):
        self.rect.centery -= 400 * dt # type: ignore
        if self.rect.bottom < 0: # type: ignore
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect= self.image.get_frect(center=pos)
        self.spawned = pygame.time.get_ticks()
        self.lifetime = 4000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)

            
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt #type: ignore . 
        if pygame.time.get_ticks() - self.spawned >= self.lifetime:
            self.kill()
            
class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = pygame.FRect = self.image.get_frect(center=(randint(0, window_width), randint(0, window_height)))
    
        
#general setup up layer_surface
pygame.init()
window_width, window_height = 1800, 1200
pygame.display.set_caption("asteroid game")
display = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True



#importing sprites
star_surf = pygame.Surface = pygame.image.load(join("images", "stars.png")).convert_alpha()
laser_surf = pygame.Surface = pygame.image.load(join("images", "laser.png")).convert_alpha()
meteor_surf= pygame.Surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()


all_sprites = pygame.sprite.Group()
laser_sprites= pygame.sprite.Group()
meteor_sprites= pygame.sprite.Group()


for i in range(20):
    star = Star(all_sprites, star_surf)
player =  Player(all_sprites)

#meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 700)

#-- MAIN LOOP --
while running:
    #dynamic fps handling
    dt = clock.tick(60) / 1000

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event: 
            x, y= randint(0, window_width), -80
            meteor = Meteor(meteor_surf, (x, y),(all_sprites, meteor_sprites))
            
            

    
    all_sprites.update(dt)

    #draw the game
    display.fill("darkblue")
    all_sprites.draw(display)

    #collision check
    pygame.sprite.groupcollide(laser_sprites, meteor_sprites, True, True)
    

    pygame.display.update()

pygame.quit()


