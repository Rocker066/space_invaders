import random

import pygame.image
from pygame.sprite import Sprite

from alien_bullet import AlienBullet


class Alien(Sprite):
    """A class to model a spaceship the user can control"""

    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()

         # Set the image
        self.image = pygame.image.load('assets/alien.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Set the initial starting position of the alien to use for reset in case of gameover
        self.starting_x = x
        self.starting_y = y

        # Set the  alien values
        self.direction = 1
        self.velocity = velocity
        self.bullet_group = bullet_group

        # Set the sound effect
        self.shoot_sound = pygame.mixer.Sound('assets/alien_fire.wav')
        self.shoot_sound.set_volume(.05)


    def update(self):
        """Update the alien movement"""
        # Move the alien horizontally based on the direction (positive or negative)
        self.rect.x += self.velocity * self.direction

        # Randomly fire a bullet
        if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()


    def fire(self):
        """Fire a bullet"""
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)


    def reset(self):
        """Reset the alien position"""
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1
