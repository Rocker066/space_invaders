import pygame.mixer
import sys
from alien import Alien


class Game:
    """A class to help control and update gameplay"""

    def __init__(self, si_game, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        # Instantiate settings and surface
        self.settings = si_game.settings
        self.screen = si_game.screen

        # Set game values
        self.round_number = 5
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
        # Determine if alien group has hit an edge
        shift = False
        for alien in self.alien_group.sprites():
            if alien.rect.left <= 0 or alien.rect.right >= self.settings.WIDTH:
                shift = True

        # Shift every alien down, change direction, and check for a breach
        if shift:
            breach = False
            for alien in self.alien_group.sprites():
                # Shift down
                alien.rect.y += 10 * self.round_number

                # Reverse the direction and move the alien off the edge so 'shift' doesn't trigger
                alien.direction *= -1
                alien.rect.x += alien.direction * alien.velocity

                # Check if an alien reached the ship
                if alien.rect.bottom >= self.settings.HEIGHT - 100:
                    breach = True

            # Aliens breached the line
            if breach:
                self.breach_sound.play()
                self.player.lives -= 1
                self.check_game_status('Aliens breached the line!', "Press ENTER to continue")


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
        self.pause_game('Space Invaders Round ' + str(self.round_number), "Press ENTER to begin")


    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
        # Empty the bullet groups and reset player and remaining aliens
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()
        self.player.reset()
        for alien in self.alien_group:
            alien.reset()

        # Check if the game is over or if it's a simple round reset
        if self.player.lives == 0:
            self.reset_game()
        else:
            self.pause_game(main_text, sub_text)


    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        # Create main pause text
        main_text = self.font.render(main_text, True, self.settings.WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2)

        sub_text = self.font.render(sub_text, True, self.settings.WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2 + 64)

        # Blit the pause text
        self.screen.fill(self.settings.BLACK)
        self.screen.blit(main_text, main_rect)
        self.screen.blit(sub_text, sub_rect)
        pygame.display.update()

        # Pause the game until the user hits Enter
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # The user wants to quit
                if event.type == pygame.QUIT:
                    sys.exit()

                # The user wants to play
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False


    def reset_game(self):
        """Reset the game"""
        self.pause_game('Final Score: ' + str(self.score), 'Press ENTER to play again')

        # Reset game values
        self.score = 0
        self.round_number = 1

        self.player.lives = 5

        # Empty groups
        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()

        # Start a new game
        self.start_new_round()


    def paused_text(self):
        self.screen.fill(self.settings.BLACK)
        paused_text = self.font.render('PAUSED', True, self.settings.WHITE)
        paused_rect = paused_text.get_rect()
        paused_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2)
        self.screen.blit(paused_text, paused_rect)
        pygame.display.update()