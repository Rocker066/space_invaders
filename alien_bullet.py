import pygame.image
from pygame.sprite import Sprite

from settings import Settings


class AlienBullet(Sprite):
    """A class to model a bullet fired by the alien"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()

        # Initiate the settings
        self.settings = Settings()

        # Set the image
        self.image = pygame.image.load('assets/red_laser.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = self.settings.ALIEN_BULLET_VELOCITY
        bullet_group.add(self)


    def update(self):
        """Update the bullet movement"""
        self.rect.y += self.velocity

        # If the bullet gets to the bottom of the screen then kill it
        if self.rect.top > self.settings.HEIGHT:
            self.kill()
