import pygame
from pygame.sprite import Sprite


class PlayerBullet(Sprite):
    """A class to model a bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()

        # Set the image
        self.image = pygame.image.load('assets/green_laser.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # Set assets
        self.velocity = 10
        bullet_group.add(self)


    def update(self):
        """Update the bullet movement"""
        self.rect.y -= self.velocity

        # If a bullet gets off the screen, then kill it
        if self.rect.bottom < 0:
            self.kill()
