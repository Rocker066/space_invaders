class Settings:
    """A class for Space Invaders' settings """

    def __init__(self):
        """Initiate the settings class attributes"""
        # Set display surface
        self.WIDTH = 1200
        self.HEIGHT = 700
        self.CAPTION = 'Space Invaders'

        # Set colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Set FPS
        self.FPS = 60

        # Set values
        self.SHOTS_FIRED = 3
        self.ALIEN_BULLET_VELOCITY = 5