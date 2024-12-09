# WINDOW #
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# BRICKS #
BRICK_TOP_CLEARANCE = 20  # Top cleareance in pixel
BRICK_BOTTOM_CLEAREANCE = WINDOW_HEIGHT / 3

BRICK_NB_BRICKS_X = 10
BRICK_NB_BRICKS_Y = 8

BRICK_MAX_LIVES = 5

BRICK_WIDTH = WINDOW_WIDTH / BRICK_NB_BRICKS_X
BRICK_HEIGHT = (
    WINDOW_HEIGHT - (BRICK_BOTTOM_CLEAREANCE + BRICK_TOP_CLEARANCE)
) / BRICK_NB_BRICKS_Y

# Colors (from lives 0 to lives x)
BRICK_COLOR_MAP = (
    (255, 0, 0),  # Red
    (168, 92, 50),  # Orange
    (242, 255, 0),  # Yellow
    (0, 255, 157),  # Green
    (0, 153, 255),  # Blue
)

# BALL #
BALL_RADIUS = 10  # Base radius
BALL_SPEED = 5  # Base speed
BALL_START_X = WINDOW_WIDTH / 2
BALL_START_Y = WINDOW_HEIGHT - BALL_RADIUS
BALL_BOUNCE_COEFFICIENT = 5  # Bouncing coefficient (see ball class)

# RACKET #
RACKET_WIDTH = 100
RACKET_HEIGHT = 10
RACKET_SPEED = 5
RACKET_COLOR = (21, 0, 255)
RACKET_BORDER_WIDTH = 5
RACKET_BORDER_COLOR = (0, 157, 255)
RACKET_START_X = WINDOW_WIDTH - RACKET_WIDTH / 2  # Start in the middle
