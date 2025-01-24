import pytest
import constants as C
from breakout import Breakout
import pygame


@pytest.fixture
def game():
    """Simulate a list of words for testing"""
    pygame.init()
    screen = pygame.display.set_mode((10, 10))
    font = pygame.font.Font("breakout/fonts/bedstead.otf", 5)

    return Breakout(screen, font)


def test_breakout_initialization(game):
    """Test the initialization of the breakout object"""
    assert game != None


def test_breakout_nb_balls(game):
    """Test if balls are generated correctly"""
    assert len(game.balls) == 1


def test_breakout_nb_bricks(game):
    """Test if bricks are generated correctly"""
    assert len(game.brick_field.bricks) == 40


def test_breakout_racket(game):
    """Test if bricks are generated correctly"""
    assert game.racket != None
