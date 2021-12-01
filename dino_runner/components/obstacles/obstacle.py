from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):

    Y_POS = 330

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[type].get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)
