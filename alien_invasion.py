import sys

import pygame

from setting import Setting

from ship import Ship

from bullet import Bullet


class AlienInvasion:
     """Overall class to manage game assets and behavior."""
     def __init__(self):
          """Intializing game and creating game resources"""
          pygame.init()
          self.clock = pygame.time.Clock()
          self.setting = Setting()

        #   self.screen = pygame.display.set_mode(
        #       (self.setting.screen_width, self.setting.screen_height))
          
          self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
          self.settings.screen_width = self.screen.get_rect().width
          self.settings.screen_height = self.screen.get_rect().height
          pygame.display.set_caption("Alien Invasion")

          self.ship = Ship(self)
          self.bullets = pygame.sprite.Group()
     
     def run_game(self):
          """Start the main loop for the game"""
          while True:
            
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

            print(len(self.bullets))

            # set the background color
            # self.bg_color = (230, 230, 230)

     def _update_bullets(self):
             """update the position of the bullets, get rid of old bullets"""
             # update bullet positions.  
             self.bullets.update()

            # get rid of bullets that have disapeared
             for bullet in self.bullets.copy():
                 if bullet.rect.bottom <=0:
                    self.bullets.remove(bullet)
                 

     def _check_events(self):
         """respond to keypresses and mouse events."""
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                  self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

     def _check_keydown_events(self, event):
        #    respond to keypresses
            if event.key == pygame.K_RIGHT:
                 self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                 sys.exit()
            elif event.key == pygame.K_SPACE:
                 self._fire_bullet()
     def _check_keyup_events(self, event):
        #   respond to keypresses
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
     def _fire_bullet(self):
            """create new bullets and add it to screen"""
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullets = Bullet(self)
                self.bullets.add(new_bullets)


     def _update_screen(self):
            """update images on the screen and flip to new screen"""
            self.screen.fill(self.setting.bg_color)
            for bullet in self.bullets.sprites():
                 bullet.draw_bullet()
            self.ship.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    # Make game instance, and rub the game
    ai = AlienInvasion()
    ai.run_game
    