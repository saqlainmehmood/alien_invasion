import sys

import pygame

from setting import Setting

from ship import Ship


class AlienInvasion:
     """Overall class to manage game assets and behavior."""
     def __init__(self):
          """Intializing game and creating game resources"""
          pygame.init()
          self.clock = pygame.time.Clock()
          self.setting = Setting()

          self.screen = pygame.display.set_mode(
              (self.setting.screen_width, self.setting.screen_height))
          pygame.display.set_caption("Alien Invasion")

          self.ship = Ship(self)
     
     def run_game(self):
          """Start the main loop for the game"""
          while True:
            
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

            # set the background color
            # self.bg_color = (230, 230, 230)

     def _check_events(self):
         """respond to keypresses and mouse events."""
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RIGHT:
                        # #   move ship to the right
                        # self.ship.rect.x += 1
                        self.ship.moving_right = True
                     elif event.key == pygame.K_LEFT:
                          self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                     if event.key == pygame.K_RIGHT:
                          self.ship.moving_right = False
                     elif event.key == pygame.K_LEFT:
                          self.ship.moving_left = False

     def _update_screen(self):
            """update images on the screen and flip to new screen"""
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    # Make game instance, and rub the game
    ai = AlienInvasion()
    ai.run_game
     