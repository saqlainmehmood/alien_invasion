from typing import Any
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """creat a bullet object at the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.setting
        self.color = self.settings.bullets_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullets position as a float
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen."""
        # update the exact position of bullet
        self.y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullets(self):
        """draw the bullets to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

        