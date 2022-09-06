import math

# game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
FPS = 60

PLAYER_POS = 1.5, 5  # MINI_MAP
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

# ray casting settings
FOV = math.tau / 6  # FOV = field of view
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20  # max intersections with walls

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)  # distance from player to screen
SCALE = WIDTH // NUM_RAYS  # scale of the wall
