import math


RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2   # 3D projection
HALF_HEIGHT = HEIGHT // 2  # 3D projection
FPS = 0

PLAYER_POS = 1.5, 5 ## mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
#Player_Size
PLAYER_SIZE_SCALE = 60

#Mouse Control
MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30) # setting floor colour

#RayCasting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE =  WIDTH // NUM_RAYS

#texture
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

