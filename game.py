import pygame.mixer
from alien import Alien


class Game:
    """A class to help control and update gameplay"""

    def __init__(self, si_game, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        # Instantiate settings and surface
        self.settings = si_game.settings
        self.screen = si_game.screen

        # Set game values
        self.round_number = 1
        self.score = 0

        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group

        # Set sound and music
        self.new_round_sound = pygame.mixer.Sound('assets/new_round.wav')
        self.new_round_sound.set_volume(.05)

        self.breach_sound = pygame.mixer.Sound('assets/breach.wav')
        self.breach_sound.set_volume(.05)

        self.alien_hit_sound = pygame.mixer.Sound('assets/alien_hit.wav')
        self.alien_hit_sound.set_volume(.05)

        self.player_hit_sound = pygame.mixer.Sound('assets/player_hit.wav')
        self.player_hit_sound.set_volume(.05)

        # Set font
        self.font = pygame.font.Font('assets/Facon.ttf', 32)


    def update(self):
        """Update the game"""
        self.shift_aliens()
        self.check_collisions()
        self.check_round_completion()


    def draw(self):
        """Draw the HUD and other information to display"""
        # Set text
        score_text = self.font.render('Score: ' + str(self.score), True, self.settings.WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = self.settings.WIDTH // 2
        score_rect.top = 10

        round_text = self.font.render('Round: ' + str(self.round_number), True, self.settings.WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)

        lives_text = self.font.render('Lives: ' + str(self.player.lives), True, self.settings.WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (self.settings.WIDTH - 20, 10)

        # Blit the HUD to the display
        self.screen.blit(score_text, score_rect)
        self.screen.blit(round_text, round_rect)
        self.screen.blit(lives_text, lives_rect)
        # Draw the lines
        pygame.draw.line(self.screen, self.settings.WHITE, (0, 50), (self.settings.WIDTH, 50), 4 )
        pygame.draw.line(self.screen, self.settings.WHITE, (0, self.settings.HEIGHT - 100),
                         (self.settings.WIDTH, self.settings.HEIGHT - 100), 4 )


    def shift_aliens(self):
        """Shift a wave of aliens down the screen and reverse direction"""
        pass


    def check_collisions(self):
        """Check for collisions"""
        pass


    def check_round_completion(self):
        """Check to see if a player has completed a single round"""
        pass


    def start_new_round(self):
        """Start a new round"""
        # Create a grid of Aliens (11 columns and 5 rows)
        for i in range(11):
            for j in range(5):
                alien = Alien(64 + (i * 64), 64 + (j * 64), self.round_number, self.alien_bullet_group)
                self.alien_group.add(alien)

        # Pause the game and prompt user to start
        self.new_round_sound.play()
        self.pause_game()


    def pause_game(self):
        """Pause the game"""
        pass


    def reset_game(self):
        """Reset the game"""
        pass


    def paused_text(self):
        self.screen.fill(self.settings.BLACK)
        paused_text = self.font.render('PAUSED', True, self.settings.WHITE)
        paused_rect = paused_text.get_rect()
        paused_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2)
        self.screen.blit(paused_text, paused_rect)
        pygame.display.update()