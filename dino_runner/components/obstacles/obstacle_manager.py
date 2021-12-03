import random


from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.lives.live import Lives


class ObstacleManager():

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.random = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if self.random == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.random == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                if game.points > 500:
                    self.obstacles.append(Bird(BIRD))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    Lives().update(game)
                    self.obstacles.remove(obstacle)
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
