from layer import Layer
import pygame
import assets
import configs


class GameOverMessage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.FLOOR
        self.image = assets.get_sprite("gameover")
        self.rect = self.image.get_rect(center = (configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 2))
        super().__init__(*groups)