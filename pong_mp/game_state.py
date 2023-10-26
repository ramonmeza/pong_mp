import dataclasses

import pygame


@dataclasses.dataclass
class GameState:
    score: tuple = dataclasses.field(default_factory=lambda: (0, 0))
    players: tuple[pygame.Vector2] = dataclasses.field(
        default_factory=lambda: (pygame.Vector2(0, 0), pygame.Vector2(0, 0))
    )
    ball: pygame.Vector2 = dataclasses.field(
        default_factory=lambda: pygame.Vector2(0, 0)
    )

    def __repr__(self) -> str:
        return f"GameState(score=({self.score[0]}, {self.score[1]}), players=(pygame.Vector2({self.players[0][0]}, {self.players[0][1]}), pygame.Vector2({self.players[1][0]}, {self.players[1][1]})), ball=pygame.Vector2({self.ball[0]}, {self.ball[1]}))"


if __name__ == "__main__":
    g = GameState()
    print(bytes(repr(g), 'utf-8'))
