from settings import*
import pygame as pg 
import math

class Player:
    def __init__(self,game):
        self.game = game
        self.x,self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        
        
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx,dy=0,0
        Speed = PLAYER_SPEED * self.game.delta_time
        Speed_sin = Speed*sin_a
        Speed_cos = Speed*cos_a
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += Speed_cos
            dy += Speed_sin
        if keys[pg.K_s]:
            dx += -Speed_cos
            dy += -Speed_sin
        if keys[pg.K_a]:
            dx += Speed_cos
            dy += -Speed_sin
        if keys[pg.K_d]:
            dx += -Speed_cos
            dy += Speed_sin
            
        self.check_wall_collision(dx,dy)
        
       # self.x += dx    without collision
       # self.y += dy
        
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
        
    def check_wall(self, x, y):
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy 
    
    def draw(self):
       # pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
       #              (self.x * 100 + WIDTH * math.cos(self.angle),
       #               self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)