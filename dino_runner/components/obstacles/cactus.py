import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS


class Cactus(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0, 2)
        if image == SMALL_CACTUS:
            super().__init__(image, self.type)
            self.rect.y = 330
        else:
            super().__init__(image, self.type)
            self.rect.y = 305
