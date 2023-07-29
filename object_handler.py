from sprite_object import*

class ObjectHandler:
    def __init__(self, game ):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'Resources/sprites/static_sprite/'
        self.anim_sprite_path = 'Resources/sprites/animated_sprite/'
        add_sprite = self.add_sprite
        
        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5,1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5,7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5,3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5,4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5,2.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5,1.5)))
        add_sprite(AnimatedSprite(game, path = self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path = self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        
    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)