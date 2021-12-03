from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class Obstacle(Sprite):

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):

        if self.image == BIRD:
            self.image_bird = self.image[self.step_index // 5]
            self.step_index += 1
            screen.blit(self.image_bird, self.rect)
            if self.step_index >= 10:
                self.step_index = 0
        else:
            screen.blit(self.image[self.type], self.rect)
