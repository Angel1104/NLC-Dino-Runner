import pygame
import pygame.draw

from dino_runner.utils.constants import HEART
from pygame.sprite import Sprite


class Lives(Sprite):
    X_POS = 750
    Y_POS = 20

    def __init__(self):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, game):
        if game.lives > 0:
            game.lives -= 1
            self.take_life(game.lives, game)
        else:
            pygame.time.delay(500)
            game.playing = False
            game.death_count += 1
            game.points = 0

    def draw(self, screen, game):
        for live in game.lives_list:
            self.rect.x = live
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def take_life(self, position, game):
        if len(game.lives_list) != 0:
            game.lives_list.pop(position)
