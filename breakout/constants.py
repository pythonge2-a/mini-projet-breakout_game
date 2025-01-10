# MENU #
TXT_FONT_SIZE = 40

# GAME #
GAME_START_LIVES = 5

# WINDOW #
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_BACKGROUND_COLOR = (150, 150, 150)

# BRICKS #
BRICK_TOP_CLEARANCE = 50  # Top cleareance in pixel
BRICK_BOTTOM_CLEAREANCE = WINDOW_HEIGHT / 2

BRICK_NB_BRICKS_X = 10
BRICK_NB_BRICKS_Y = 8

BRICK_MAX_LIVES = 5

BRICK_HORIZONTAL_SPACING = 2  # Espace horizontal entre les briques
BRICK_VERTICAL_SPACING = 2  # Espace vertical entre les briques

BRICK_WIDTH = (
    WINDOW_WIDTH - (BRICK_NB_BRICKS_X - 1) * BRICK_HORIZONTAL_SPACING
) / BRICK_NB_BRICKS_X
BRICK_HEIGHT = (
    (WINDOW_HEIGHT - (BRICK_BOTTOM_CLEAREANCE + BRICK_TOP_CLEARANCE))
    - (BRICK_NB_BRICKS_Y - 1) * BRICK_VERTICAL_SPACING
) / BRICK_NB_BRICKS_Y

# Colors (from lives 0 to lives x)
BRICK_COLOR_MAP = (
    (0, 0, 0),  # Dead
    (206, 189, 167),  # sable
    (148, 80, 66),  # petit cailloux
    (210, 173, 155),  # moyen cailloux
    (213, 203, 189),  # gros cailloux
    (95, 91, 90),  # brique
)

BRICK_BORDER_WIDTH = 4
BRICK_BORDER_COLOR_FACTOR = 0.5

# BALL #
BALL_RADIUS = 10  # Base radius
BALL_SPEED = 5  # Base speed

BALL_START_X = WINDOW_WIDTH / 2
BALL_START_Y = WINDOW_HEIGHT - 20 - 2 * BALL_RADIUS

BALL_BOUNCE_COEFFICIENT = 5  # Bouncing coefficient (see ball class)
BALL_COLOR = (255, 0, 64)

# RACKET #
RACKET_WIDTH = 100
RACKET_HEIGHT = 15
RACKET_SPEED = 5
RACKET_COLOR = (21, 0, 255)
RACKET_BORDER_WIDTH = 2
RACKET_BORDER_COLOR = (0, 157, 255)

RACKET_START_X = WINDOW_WIDTH / 2 - RACKET_WIDTH / 2  # Start in the middle
RACKET_START_Y = WINDOW_HEIGHT - 20

RACKET_BORDER_RADIUS = 3

# LEVELS #
LEVELS_NUMBER = 5
LEVELS_MAPS = [
    "1111111111"
    "1222222221"
    "1233333321"
    "1234554321"
    "1234554321"
    "1233333321"
    "1222222221"
    "1111111111",
    "1111111111"
    "1111111111"
    "1111111111"
    "1111111111"
    "1111221111"
    "3333333333"
    "4444444444"
    "4444444444",
    "1111111111"
    "1111111111"
    "1111111111"
    "1111111111"
    "1111221111"
    "3333333333"
    "4444444444"
    "4444444444",
    "1111111111"
    "1111111111"
    "1111111111"
    "1111111111"
    "1111221111"
    "3333333333"
    "4444444444"
    "4444444444",
    "1111111111"
    "1111111111"
    "1111111111"
    "1111111111"
    "1111221111"
    "3333333333"
    "4444444444"
    "4444444444",
]

LEVEL_RECT_X = WINDOW_WIDTH - 10
LEVEL_RECT_Y = 10

LEVEL_FONT_COLOR = (33, 33, 33)

# BONUS #
BONUS_WIDTH = BRICK_WIDTH / 2
BONUS_HEIGHT = BRICK_HEIGHT / 2
BONUS_POS_X = 19
BONUS_POS_Y = 15
BONUS_SPEED = 2
BONUS_QUANTITY = int((BRICK_NB_BRICKS_X * BRICK_NB_BRICKS_Y) / 1)
ACTIVATION_TIME = 1000
RACKET_GROW_SIZE = 20
RACKET_SHRINK_SIZE = 20
RACKET_SPEED_UP = 5
RACKET_SPEED_DOWN = 1
BALL_GROW_SIZE = 5
BALL_SHRINK_SIZE = 1
BALL_SPEED_DOWN = 2
BALL_SPEED_UP = 1
BRICK_ADD_LIFE = 1
NET_REBOUNDS = 3
NET_POS = [1, WINDOW_HEIGHT - 10]
NET_SIZE = [WINDOW_WIDTH, 10]

# SCORE #
SCORE_RECT_X = 10
SCORE_RECT_Y = 10

SCORE_FONT_COLOR = LEVEL_FONT_COLOR

# LIVES #
LIVES_RECT_X = WINDOW_WIDTH / 2 - 100
LIVES_RECT_Y = 10

LIVES_FONT_COLOR = LEVEL_FONT_COLOR

# ANIMATION #
ANIMATION_LIFETIME = 50
ANIMATION_NUMBER_OF_FRAGMENTS = 100

# TILESET #
TILESET_PATH = "breakout/tileset/Tileset V4.png"
TILESET_BRICKS_POS = [1, 1]
TILESET_BRICKS_SIZE = [78, 30]

TILESET_BALLS_POS = [119, 1]
TILESET_BALLS_SIZE = [21, 21]

TILESET_RACKETS_POS = [140, 1]
TILESET_RACKETS_SIZE = [100, 15]

TILESET_BONUSES_POS = [80, 1]
TILESET_BONUSES_SIZE = [38, 14]
TILESET_NET_POS = [1, 1]
TILESET_NET_SIZE = [WINDOW_WIDTH, 10]
TILESET_GHOST_POS = [TILESET_BALLS_POS[0], TILESET_BALLS_POS[1] + TILESET_BALLS_SIZE[0]]
TILESET_UNSTOPPABLE_POS = [
    TILESET_BALLS_POS[0],
    TILESET_BALLS_POS[1] + TILESET_BALLS_SIZE[0] * 3,
]
TILESET_GLU_POS = [
    TILESET_BALLS_POS[0],
    TILESET_BALLS_POS[1] + TILESET_BALLS_SIZE[0] * 2,
]
TILESET_EXPL_POS = [
    TILESET_BALLS_POS[0],
    TILESET_BALLS_POS[1] + TILESET_BALLS_SIZE[0] * 4,
]
