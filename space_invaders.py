import pygame, random

from settings import Settings
from player import Player
from game import Game


class SpaceInvaders:
    """The main class for Space Invaders game"""

    def __init__(self):
        """Set the attributes"""
        # Initialize pygame
        pygame.init()

        # Instantiate the settings object
        self.settings = Settings()

        # Set the display surface and caption
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption(self.settings.CAPTION)

        # Set the state of the game
        self.running = True
        self.game_paused = False

        # Set Clock
        self.clock = pygame.time.Clock()

        # Create bullet groups
        self.my_player_bullet_group = pygame.sprite.Group()
        self.my_alien_bullet_group = pygame.sprite.Group()

        # Create a player group and player object
        self.my_player_group = pygame.sprite.Group()
        self.my_player = Player(self.my_player_bullet_group)
        self.my_player_group.add(self.my_player)

        # Create an alien group (will add Alien objects via the Game class' start_new_round method)
        self.my_alien_group = pygame.sprite.Group()

        # Create a Game object
        self.my_game = Game(self, self.my_player, self.my_alien_group,
                            self.my_player_bullet_group, self.my_alien_bullet_group)
        self.my_game.start_new_round()


    def run_game(self):
        """The main loop of the game"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # The player wants to fire
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.my_player.fire()

                    # Player presses Esc key to pause and unpause the game
                    if event.key == pygame.K_ESCAPE:
                        self.my_game.paused_text()
                        self.game_paused = not self.game_paused

            # Update the screen
            self.update()


    def update(self):
        """Update and fill the screen and assets and tick the clock"""
        # Fill the screen
        self.screen.fill(self.settings.BLACK)

        if not self.game_paused:
            # Update and display all sprite groups
            self.my_player_group.update()
            self.my_player_group.draw(self.screen)

            self.my_alien_group.update()
            self.my_alien_group.draw(self.screen)

            self.my_player_bullet_group.update()
            self.my_player_bullet_group.draw(self.screen)

            self.my_alien_bullet_group.update()
            self.my_alien_bullet_group.draw(self.screen)

            # Update and draw the Game object
            self.my_game.update()
            self.my_game.draw()

            # Update the screen and tick the clock
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)



if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
