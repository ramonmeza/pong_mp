import pygame

from pong_mp.game_state import GameState


def test_init():
    game_state: GameState = GameState()

    assert isinstance(game_state.score, tuple)
    assert len(game_state.score) == 2
    assert game_state.score[0] == 0
    assert game_state.score[1] == 0

    assert isinstance(game_state.players, tuple)
    assert len(game_state.players) == 2

    assert isinstance(game_state.players[0], pygame.Vector2)
    assert game_state.players[0].x == 0
    assert game_state.players[0].y == 0

    assert isinstance(game_state.players[1], pygame.Vector2)
    assert game_state.players[1].x == 0
    assert game_state.players[1].y == 0

    assert isinstance(game_state.ball, pygame.Vector2)
    assert game_state.ball.x == 0
    assert game_state.ball.y == 0


def test_repr():
    game_state: GameState = GameState()
    assert eval(repr(game_state)) == game_state
