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
BALL_RADIUS = 13  # Base radius
BALL_SPEED = 6  # Base speed

BALL_START_X = WINDOW_WIDTH / 2
BALL_START_Y = WINDOW_HEIGHT - 20 - 2 * BALL_RADIUS

BALL_BOUNCE_COEFFICIENT = 5  # Bouncing coefficient (see ball class)
BALL_COLOR = (255, 0, 64)

# RACKET #
RACKET_WIDTH = 100
RACKET_HEIGHT = 15
RACKET_SPEED = 8
RACKET_COLOR = (21, 0, 255)
RACKET_BORDER_WIDTH = 2
RACKET_BORDER_COLOR = (0, 157, 255)

RACKET_START_X = WINDOW_WIDTH / 2 - RACKET_WIDTH / 2  # Start in the middle
RACKET_START_Y = WINDOW_HEIGHT - 20

RACKET_BORDER_RADIUS = 3

# LEVELS #
LEVELS_NUMBER = 33
LEVELS_MAPS = [
    "1212121212"
    "0000000000"
    "2121212121"
    "0000000000"
    "1212121212"
    "0000000000"
    "2121212121"
    "0000000000",  # 0

    "3334423333"
    "0333443000"
    "0222233200"
    "0022143320"
    "0021223200"
    "0212002000"
    "0212000000"
    "0010000000",  # 1

    "5432112345"
    "0000000000"
    "3223003223"
    "0000000000"
    "5445005445"
    "0000000000"
    "5555115555"
    "0000000000",  # 2

    "0001221000"
    "0013333100"
    "0125555210"
    "1255555521"
    "1234444321"
    "0123333210"
    "0012222100"
    "0001111000",  # 3

    "0000000000"
    "0055005500"
    "5555555555"
    "0555555550"
    "0055555500"
    "0005555000"
    "0000550000"
    "0000000000",  # 4

    "5555555555"
    "4444004444"
    "0330000330"
    "0220000220"
    "0220000220"
    "0330000330"
    "4444004444"
    "5555555555",  # 5

    "0003333000"
    "0033333300"
    "0333333330"
    "0300440030"
    "0000440000"
    "0000440000"
    "0444444440"
    "4444444444",  # 6

    "0000300050"
    "3010000050"
    "3010304001"
    "0020304001"
    "0020003000"
    "1004403500"
    "1004400504"
    "0004400004",  # 7

    "0050050500"
    "0005000050"
    "0500005000"
    "0005000500"
    "0500050005"
    "0005000500"
    "0500050050"
    "0005000500",  # 8

    "5550000000"
    "5555000330"
    "5550500330"
    "0000055444"
    "0000004444"
    "0055500444"
    "0550050444"
    "5500005555",  # 9

    "0001221000"
    "0012332100"
    "0123454321"
    "1234555432"
    "1234555432"
    "0123454321"
    "0012332100"
    "0001221000",  # 10

    "0000000000"
    "0000040000"
    "0000440000"
    "0044430000"
    "0444433000"
    "0441333320"
    "4411333322"
    "4111122222",  # 11

    "0000555000"
    "0005222500"
    "0052222250"
    "0052252250"
    "0052225250"
    "5205552250"
    "0522222500"
    "0055555000",  # 12

    "0000000000"
    "0020000200"
    "0222002220"
    "0222002220"
    "2442222442"
    "4444444444"
    "4444444444"
    "4444444444",  # 13

    "0000000004"
    "0000000444"
    "0000004444"
    "0000444444"
    "0000444444"
    "3333444444"
    "0003333333"
    "0000033333",  # 14

    "0001221000"
    "0012332100"
    "0123454321"
    "1234555432"
    "1234555432"
    "0123454321"
    "0012332100"
    "0001221000",  # 15

    "0005550000"
    "0005552222"
    "0005550000"
    "4444444440"
    "0044444440"
    "0004444000"
    "0000444000"
    "0444444440",  # 16

    "0000000022"
    "0020000002"
    "0222000000"
    "0020000550"
    "0000005555"
    "0040005555"
    "0444000550"
    "0040000000",  # 17

    "0002332000"
    "0002332000"
    "0034444300"
    "0344444430"
    "0344444430"
    "0034444300"
    "0002332000"
    "0002332000",  # 18

    "0000000000"
    "0055005500"
    "0000000000"
    "5550000555"
    "0500440050"
    "0500440050"
    "0550000550"
    "0000000000",  # 19

    "0000000000"
    "0550000550"
    "0540000450"
    "0000000000"
    "0005555000"
    "0055555500"
    "0550000550"
    "0550000550",  # 20

    "0001221000"
    "0012332100"
    "0123454321"
    "1234555432"
    "1234555432"
    "0123454321"
    "0012332100"
    "0001221000",  # 21

    "0000000000"
    "5505550555"
    "0555055505"
    "5505550555"
    "0000000000"
    "5055505550"
    "5550555055"
    "5055505550",  # 22

    "2030120302"
    "2030210302"
    "2030120302"
    "2030210302"
    "2030120302"
    "2030210302"
    "2030120302"
    "2030210302",  # 23

    "1234554321"
    "0102030405"
    "1234554321"
    "0102030405"
    "1234554321"
    "0102030405"
    "1234554321"
    "0102030405",  # 24

    "0000220000"
    "0022332200"
    "0233113320"
    "2331111332"
    "2331111332"
    "0233113320"
    "0022332200"
    "0000220000",  # 25

    "0000440000"
    "0044004400"
    "0400220040"
    "4002222004"
    "4002222004"
    "0400220040"
    "0044004400"
    "0000440000",  # 26

    "0000330000"
    "0003333000"
    "0333223330"
    "0321111230"
    "3321001233"
    "3210000123"
    "3250000523"
    "3210000123",  # 27

    "5400000045"
    "4000330004"
    "0003223000"
    "0032112300"
    "0032112300"
    "0003223000"
    "4000330004"
    "5400000045",  # 28

    "3000000335"
    "5400004000"
    "0033003400"
    "0000110000"
    "0003030000"
    "0040003000"
    "0040000440"
    "5500000055",  # 29

    "0000433400"
    "0004400440"
    "0550000005"
    "0043000055"
    "0004404400"
    "0000330000"
    "0000220000"
    "0002112000",  # 30

    "4000110042"
    "0002200200"
    "0033011000"
    "0002201000"
    "0000100100"
    "0001100100"
    "0022000220"
    "2200000022",  # 31

    "4332112334"
    "4433223344"
    "0443333440"
    "0044444400"
    "0000000000"
    "1100000011"
    "0110000110"
    "0001111000",  # 32

]

LEVEL_RECT_X = WINDOW_WIDTH - 10
LEVEL_RECT_Y = 10

LEVEL_FONT_COLOR = (250, 250, 250)

# BONUS #
BONUS_WIDTH = BRICK_WIDTH / 2
BONUS_HEIGHT = BRICK_HEIGHT / 2
BONUS_POS_X = 19
BONUS_POS_Y = 15
BONUS_SPEED = 2
ACTIVATION_TIME = 1000
RACKET_GROW_SIZE = 20
RACKET_SHRINK_SIZE = 20
RACKET_SPEED_UP = 2
RACKET_SPEED_DOWN = 1
BALL_GROW_SIZE = 5
BALL_SHRINK_SIZE = 1
BALL_SPEED_DOWN = 2
BALL_SPEED_UP = 1
BRICK_ADD_LIFE = 1
NET_REBOUNDS = 3
NET_POS = [1, WINDOW_HEIGHT - 10]
NET_SIZE = [WINDOW_WIDTH, 10]
MAX_EXPLOSION = 5
SPEED_EXPLOSION = 3
GHOST_BOUNCES = 1
UNSTOP_BOUNCES = 1

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
TILESET_PATH = "breakout/tileset/Tileset cristaux.png"
TILESET_BRICKS_POS = [1, 1]
TILESET_BRICKS_SIZE = [78, 30]

TILESET_BALLS_POS = [119, 1]
TILESET_BALLS_SIZE = [21, 21]

TILESET_RACKETS_POS = [140, 1]
TILESET_RACKETS_SIZE = [100, 15]

TILESET_BONUSES_POS = [80, 1]
TILESET_BONUSES_SIZE = [38, 14]
TILESET_NET_POS = [240, 1]
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
TILESET_REVERSE_POS = [
    TILESET_RACKETS_POS[0],
    TILESET_RACKETS_POS[1] + TILESET_RACKETS_SIZE[1] + 1,
]
TILESET_INVISIBLE_POS = [
    TILESET_RACKETS_POS[0],
    TILESET_RACKETS_POS[1] + 2 * TILESET_RACKETS_SIZE[1] + 1,
]
