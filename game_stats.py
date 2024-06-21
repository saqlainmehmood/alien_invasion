class GameStats:
    """Track stats for alien invasion"""

    def __init__ (self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.prep_level()

        # high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """intializw statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def prep_level(self):
        """turn the level into a rendered the image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
