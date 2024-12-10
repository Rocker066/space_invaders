import pygame.image
from pygame.sprite import Sprite

from settings import Settings
from player_bullet import PlayerBullet


class Player(Sprite):
    """A class to model a spaceship the user can control"""

    def __init__(self, bullet_group):
        """Initialize the player"""
        super().__init__()

        # Instantiate the settings
        self. settings = Settings()

        # Set player image
        self.image = pygame.image.load('assets/player_ship.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.WIDTH // 2
        self.rect.bottom = self.settings.HEIGHT

        # Set player values
        self.lives = 5
        self.velocity = 8

        self.bullet_group = bullet_group

        # Set sound effects
        self.shoot_sound = pygame.mixer.Sound('assets/player_fire.wav')
        self.shoot_sound.set_volume(.05)


    def update(self):
        """Update the player movement"""
        # Define Continuous movement
        keys = pygame.key.get_pressed()

        # Move the player's ship horizontally within the bounds of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < self.settings.WIDTH:
            self.rect.x += self.velocity


    def fire(self):
        """Fire a bullet"""
        # Restrict the number of bullets fired at a time
        if len(self.bullet_group) < self.settings.SHOTS_FIRED:
            self.shoot_sound.play()
            # Instantiate a bullet object
            PlayerBullet(self.rect.centerx, self.rect.centery, self.bullet_group)


    def reset(self):
        """Reset the player position"""
        self.rect.x = self.settings.WIDTH // 2
